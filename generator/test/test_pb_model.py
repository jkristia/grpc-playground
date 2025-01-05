from typing import Any, cast
import unittest
from google.protobuf.json_format import MessageToDict
from generator_test import module_a_pb2, module_b_pb2
from descriptors import FieldType, ModelFieldDescriptor, ModelGeneratorDoc, ModelModuleDescriptor, ModelMessageDescriptor 
from model_autogen import ModelBase, ModelBasicMessageA, ModelBasicEnum, ModelBasicMessageB, ModelBasicSubItem, ModelSomePoint

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
        b = msg.HasField(ModelBasicMessageA.PB_O_INT_VALUE)
        assert b == True
        v = getattr(msg, ModelBasicMessageA.PB_O_INT_VALUE)
        assert v == 123
        # int_value is not 'optional' so it will return default value
        v = getattr(msg, ModelBasicMessageA.PB_INT_VALUE)
        assert v == 0
        
        data = ModelBase.dict_from_pb_message(msg)
        assert data.get(ModelBasicMessageA.INT_VALUE) == 0
        assert data.get(ModelBasicMessageA.O_INT_VALUE) == 123
        assert data.get(ModelBasicMessageA.BOOL_VALUE) == False
        assert data.get(ModelBasicMessageA.O_BOOL_VALUE) == None
    
    def test_serialize_enum(self):
        pb_msg = module_a_pb2.BasicMessageA(
            name='msg1',
            bool_value=True,
            enum_value=module_a_pb2.BasicEnum.VALUE_1,
            o_int_value=123
        )
        data = ModelBasicMessageA.dict_from_pb_message(pb_msg)
        # instantiating by passing args in constructor will not create the enum value correct
        msg = ModelBasicMessageA(**data)
        assert msg.name == 'msg1'
        assert msg.enumValue == 'VALUE_1' # this is incorrect
        assert (msg.enumValue == ModelBasicEnum.VALUE_1) == False
        # instantiating using from_dict will setup the enums correct
        msg = ModelBasicMessageA.from_dict(data)
        assert msg.name == 'msg1'
        assert msg.enumValue != 'VALUE_1' 
        assert (msg.enumValue == ModelBasicEnum.VALUE_1) == True
        
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
        msg = ModelBasicMessageA.from_pb_msg(pb_msg)
        assert isinstance(msg, ModelBasicMessageA)
        assert isinstance(msg.enumValue, ModelBasicEnum)
        assert msg.name == 'msg1'
        assert (msg.enumValue == ModelBasicEnum.VALUE_1) == True
        assert msg.subItem is not None
        assert isinstance(msg.subItem, ModelBasicSubItem)
        assert msg.subItem.name == 'sub1'
        assert isinstance(msg.subItem.singlePoint, ModelSomePoint)
        assert msg.subItem.singlePoint.y == 2
        
        
        
        
