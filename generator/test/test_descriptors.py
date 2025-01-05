from typing import Any, cast
import unittest
from generator_test import module_a_pb2, module_b_pb2
from descriptors import FieldType, ModelFieldDescriptor, ModelGeneratorDoc, ModelModuleDescriptor, ModelMessageDescriptor 

class TestDescriptors(unittest.TestCase):
    
    def setUp(self):
        self.doc = ModelGeneratorDoc([
            module_a_pb2.DESCRIPTOR,
            module_b_pb2.DESCRIPTOR
        ])
    
    def getBasicMessageA(self) -> ModelMessageDescriptor:
        module = cast(ModelModuleDescriptor, self.doc.find_module('module_a'))
        message = cast(ModelMessageDescriptor, module.find_message('BasicMessageA'))
        return message
    
    def test_load(self):
        doc = self.doc
        assert doc.model_prefix == 'Model'
        assert len(doc.modules) == 2
        assert doc.modules[0].name == 'module_a'
        assert doc.modules[1].name == 'module_b'
        
        modulename = 'module_a'
        module = doc.find_module(modulename)
        assert module is not None
        assert module.name == modulename
        
        modulename = 'module_b'
        module = doc.find_module(modulename)
        assert module is not None
        assert module.name == modulename
        
        modulename = 'module_xyz'
        module = doc.find_module(modulename)
        assert module is None
    pass

    def test_find_message(self):
        doc = self.doc
        module = doc.find_module('module_a')
        assert module is not None
        message = module.find_message('BasicMessageA')
        assert message is not None
        assert message.name == 'BasicMessageA'
        assert message.class_name == 'ModelBasicMessageA'
        pass
    
    def test_message_fields(self):
        msg = self.getBasicMessageA()
        fields_as_string = ', '.join([ f.json_name for f in msg.fields])
        print(fields_as_string)
        assert fields_as_string == 'name, intValue, floatValue, boolValue, enumValue, repeatedField, subItem, ' \
                                    'oName, oIntValue, oFloatValue, oBoolValue, oEnumValue'
        field = cast(ModelFieldDescriptor, msg.find_field('name'))
        #
        # field with no 'optional' in .proto are still optional by default
        #
        assert field.json_name == 'name'
        assert field.property_type == FieldType.str
        assert field.is_optional == True # all fields are optional in proto3
        field = cast(ModelFieldDescriptor, msg.find_field('intValue'))
        assert field.json_name == 'intValue'
        assert field.property_type == FieldType.int
        assert field.is_optional == True # all fields are optional in proto3
        field = cast(ModelFieldDescriptor, msg.find_field('floatValue'))
        assert field.json_name == 'floatValue'
        assert field.property_type == FieldType.float
        field = cast(ModelFieldDescriptor, msg.find_field('boolValue'))
        assert field.json_name == 'boolValue'
        assert field.property_type == FieldType.bool
        field = cast(ModelFieldDescriptor, msg.find_field('enumValue'))
        assert field.json_name == 'enumValue'
        assert field.property_type == FieldType.enum
        assert field.is_repeated == False
        field = cast(ModelFieldDescriptor, msg.find_field('subItem'))
        assert field.json_name == 'subItem'
        assert field.property_type == FieldType.cls
        assert field.object_type == 'module_a.BasicSubItem'
        #
        # repeated
        #
        field = cast(ModelFieldDescriptor, msg.find_field('repeatedField'))
        assert field.json_name == 'repeatedField'
        assert field.property_type == FieldType.int
        assert field.is_optional == True # all fields are optional in proto3
        assert field.is_repeated == True
        #
        # optional fields
        #
        field = cast(ModelFieldDescriptor, msg.find_field('oName'))
        assert field.json_name == 'oName'
        assert field.property_type == FieldType.str
        assert field.is_optional == True
        field = cast(ModelFieldDescriptor, msg.find_field('oIntValue'))
        assert field.json_name == 'oIntValue'
        assert field.property_type == FieldType.int
        assert field.is_optional == True
        field = cast(ModelFieldDescriptor, msg.find_field('oFloatValue'))
        assert field.json_name == 'oFloatValue'
        assert field.property_type == FieldType.float
        assert field.is_optional == True
        field = cast(ModelFieldDescriptor, msg.find_field('oBoolValue'))
        assert field.json_name == 'oBoolValue'
        assert field.property_type == FieldType.bool
        assert field.is_optional == True
        field = cast(ModelFieldDescriptor, msg.find_field('oEnumValue'))
        assert field.json_name == 'oEnumValue'
        assert field.property_type == FieldType.enum
        assert field.is_optional == True
        


if __name__ == '__main__':
    unittest.main()
    
    
