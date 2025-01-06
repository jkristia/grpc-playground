from typing import Any, cast
import unittest
from google.protobuf.json_format import MessageToDict
from generator_test import module_a_pb2, module_b_pb2
from descriptors import FieldType, ModelFieldDescriptor, ModelGeneratorDoc, ModelModuleDescriptor, ModelMessageDescriptor 
from model_autogen import ModelBase, ModuleA_BasicMessageA, ModuleA_BasicEnum, ModuleA_BasicSubItem, ModuleA_MsgWithOneOfProps, ModuleA_MsgWithRepeatedProps, ModuleA_MsgWithSet, ModuleA_SomePoint, ModuleB_ItemB

class TestPb2Model(unittest.TestCase):
    
    def setUp(self):
        self.doc = ModelGeneratorDoc(
            modules=[
                module_a_pb2.DESCRIPTOR,
                module_b_pb2.DESCRIPTOR
            ],
            )
        self.module = cast(ModelModuleDescriptor, self.doc.find_module('module_a'))
        
    def test_field_constants(self):
        msg = module_a_pb2.BasicMessageA(
            o_int_value=123
        )
        # hasfield can only be use of fields defined with 'optional'
        b = msg.HasField(ModuleA_BasicMessageA.PB_O_INT_VALUE)
        assert b == True
        v = getattr(msg, ModuleA_BasicMessageA.PB_O_INT_VALUE)
        assert v == 123
        # int_value is not 'optional' so it will return default value
        v = getattr(msg, ModuleA_BasicMessageA.PB_INT_VALUE)
        assert v == 0
        
        data = ModelBase.dict_from_pb_message(msg)
        assert data.get(ModuleA_BasicMessageA.INT_VALUE) == 0
        assert data.get(ModuleA_BasicMessageA.O_INT_VALUE) == 123
        assert data.get(ModuleA_BasicMessageA.BOOL_VALUE) == False
        assert data.get(ModuleA_BasicMessageA.O_BOOL_VALUE) == None
    
    def test_serialize_enum(self):
        pb_msg = module_a_pb2.BasicMessageA(
            name='msg1',
            bool_value=True,
            enum_value=module_a_pb2.BasicEnum.VALUE_1,
            o_int_value=123
        )
        data = ModuleA_BasicMessageA.dict_from_pb_message(pb_msg)
        # instantiating by passing args in constructor will not create the enum value correct
        msg = ModuleA_BasicMessageA(**data)
        assert msg.name == 'msg1'
        assert msg.enumValue == 'VALUE_1' # this is incorrect
        assert (msg.enumValue == ModuleA_BasicEnum.VALUE_1) == False
        # instantiating using from_dict will setup the enums correct
        msg = ModuleA_BasicMessageA.from_dict(data)
        assert msg.name == 'msg1'
        assert msg.enumValue != 'VALUE_1' 
        assert (msg.enumValue == ModuleA_BasicEnum.VALUE_1) == True
        
    def test_from_pb_msg(self):
        # create protobuf message
        pb_msg = module_a_pb2.BasicMessageA(
            name='msg1',
            bool_value=True,
            enum_value=module_a_pb2.BasicEnum.VALUE_1,
            o_int_value=123,
            sub_item=module_a_pb2.BasicSubItem(
               name='sub1',
               singlePoint=module_a_pb2.SomePoint(x=1, y=2)
            )
        )
        # instantiate model from protobuf instance
        msg = ModuleA_BasicMessageA.from_pb_msg(pb_msg)
        assert isinstance(msg, ModuleA_BasicMessageA)
        assert isinstance(msg.enumValue, ModuleA_BasicEnum)
        assert msg.name == 'msg1'
        assert (msg.enumValue == ModuleA_BasicEnum.VALUE_1) == True
        assert msg.subItem is not None
        assert isinstance(msg.subItem, ModuleA_BasicSubItem)
        assert msg.subItem.name == 'sub1'
        assert isinstance(msg.subItem.singlePoint, ModuleA_SomePoint)
        assert msg.subItem.singlePoint.y == 2
        
    def test_repeated_values(self):
        # create protobuf message
        pb_msg = module_a_pb2.MsgWithRepeatedProps(
            txt='some text',
            lines=['line1', 'line2'],
            enums=[module_a_pb2.BasicEnum.VALUE_1, module_a_pb2.BasicEnum.ABC],
            points=[
                module_a_pb2.SomePoint(x=1, y=2),
                module_a_pb2.SomePoint(x=2, y=3),
                module_a_pb2.SomePoint(x=3, y=4),
            ]
        )
        msg = ModuleA_MsgWithRepeatedProps.from_pb_msg(pb_msg)
        assert msg.txt == 'some text'
        assert msg.lines == ['line1', 'line2']
        assert msg.enums is not None
        assert msg.enums == [ModuleA_BasicEnum.VALUE_1, ModuleA_BasicEnum.ABC]
        for enum in msg.enums:
            assert isinstance(enum, ModuleA_BasicEnum)
        assert msg.points is not None
        assert len(msg.points) == 3
        for point in msg.points:
            assert isinstance(point, ModuleA_SomePoint)
        assert msg.points[0].x == 1
        assert msg.points[1].x == 2
        assert msg.points[2].x == 3
        
    def test_repeated_clone(self):
        pb_msg = module_a_pb2.MsgWithRepeatedProps(
            txt='some text',
            lines=['line1', 'line2'],
            enums=[module_a_pb2.BasicEnum.VALUE_1, module_a_pb2.BasicEnum.ABC],
            points=[
                module_a_pb2.SomePoint(x=1, y=2),
                module_a_pb2.SomePoint(x=2, y=3),
                module_a_pb2.SomePoint(x=3, y=4),
            ]
        )
        msg = ModuleA_MsgWithRepeatedProps.from_pb_msg(pb_msg)
        ### check dict
        d = msg.to_dict()
        ### clone ###
        clone = msg.clone()
        msg.txt = ''
        msg.lines = []
        assert clone.txt == 'some text'
        assert clone.lines == ['line1', 'line2']
        assert clone.enums is not None
        assert clone.enums == [ModuleA_BasicEnum.VALUE_1, ModuleA_BasicEnum.ABC]
        for enum in clone.enums:
            assert isinstance(enum, ModuleA_BasicEnum)
        assert clone.points is not None
        assert len(clone.points) == 3
        for point in clone.points:
            assert isinstance(point, ModuleA_SomePoint)
        assert clone.points[0].x == 1
        assert clone.points[1].x == 2
        assert clone.points[2].x == 3
        
    def test_oneof(self):
        pb_msg = module_a_pb2.MsgWithOneOfProps(
            txt='some text',
            point_a=module_a_pb2.SomePoint(x=1, y=2),
            point_b=module_a_pb2.SomePoint(x=3, y=4),
        )
        msg = ModuleA_MsgWithOneOfProps.from_pb_msg(pb_msg)
        assert msg.pointA == None
        assert msg.pointB != None
        assert msg.pointB.x == 3
        msg.pointA = ModuleA_SomePoint(x=5, y=6)
        assert msg.pointA != None
        assert msg.pointB == None
        assert msg.pointA.x == 5

    def test_map(self):
        pb_msg = module_a_pb2.MsgWithSet(
            a_string_map={'a': '123', 'b': '456'},
            items_map={
                '44': module_b_pb2.ItemB(id=44),
                '55': module_b_pb2.ItemB(id=55),
            }
        )
        msg = ModuleA_MsgWithSet.from_pb_msg(pb_msg)
        assert msg._aStringMap == {'a': '123', 'b': '456'}
        assert msg.item == None
        assert msg.itemsMap is not None
        assert len(msg.itemsMap.values()) == 2
        assert isinstance(msg.itemsMap['44'], ModuleB_ItemB)
        assert msg.itemsMap['44'].id == 44
        assert isinstance(msg.itemsMap['55'], ModuleB_ItemB)
        assert msg.itemsMap['55'].id == 55
