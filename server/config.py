from typing import Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import json

from descriptors import ModelGeneratorDoc

class ValueType(Enum):
    UNKNOWN = 'UNKNOWN'
    TYPE_A = 'TYPE_A'
    TYPE_B = 'TYPE_B'

@dataclass
class ModelBase():
    def to_dict(self) -> Any:
        return self._to_dict(asdict(self))
    
    def _to_dict(self, obj) -> Any:
        # return enum name, not value
        if isinstance(obj, Enum):
            return obj.name
        # remove None values
        if isinstance(obj, list):
            return [self._to_dict(item) for item in obj if item is not None]
        if isinstance(obj, dict):
            return {key: self._to_dict(value) for key, value in obj.items() if value is not None }
        else:
            return obj
        
    def after_serialize_in(self) -> Any:
        return self

@dataclass
class ModelFooA(ModelBase):
    id: str
    type: ValueType
    name: Optional[str] = None
    value: Optional[int] = None
    type_optional: Optional[ValueType] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ModelFooA':
        return cls(**data).after_serialize_in()

    def after_serialize_in(self) -> 'ModelFooA':
        if self.type is not None:
            self.type = ValueType(self.type)
        if self.type_optional is not None:
            self.type_optional = ValueType(self.type_optional)
        return self

    def clone(self) -> 'ModelFooA':
        return ModelFooA.from_dict(self.to_dict())

@dataclass
class ModelFooB(ModelBase):
    id: str
    enabled: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> 'ModelFooB':
        return cls(**data).after_serialize_in()

    def after_serialize_in(self) -> 'ModelFooB':
        return self

    def clone(self) -> 'ModelFooB':
        return ModelFooB.from_dict(self.to_dict())

@dataclass
class ModelConfig(ModelBase):
    
    id: str
    fooA: Optional[ModelFooA] = None
    fooB: Optional[ModelFooB] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ModelConfig':
        return cls(**data).after_serialize_in()

    def after_serialize_in(self) -> 'ModelConfig':
        if self.fooA is not None:
            raw: Any = self.fooA
            self.fooA = ModelFooA(**raw).after_serialize_in()
        if self.fooB is not None:
            raw: Any = self.fooB
            self.fooB = ModelFooB(**raw).after_serialize_in()
            
        return self

    def clone(self) -> 'ModelConfig':
        return ModelConfig.from_dict(self.to_dict())


import google.protobuf.message
from google.protobuf.descriptor import Descriptor, FieldDescriptor
from google.protobuf.json_format import MessageToJson, MessageToDict, ParseDict
import config_pb2

class FieldType(Enum):
    cls = 'class'
    str = 'str'
    int = 'int'
    enum = 'enum'
    bool = 'bool'

def map_field_type(field_type: int) -> FieldType | str:
    if field_type == FieldDescriptor.TYPE_INT32:
        return FieldType.int
    if field_type == FieldDescriptor.TYPE_INT64:
        return FieldType.int
    if field_type == FieldDescriptor.TYPE_BOOL:
        return FieldType.bool
    if field_type == FieldDescriptor.TYPE_STRING:
        return FieldType.str
    if field_type == FieldDescriptor.TYPE_MESSAGE:
        return FieldType.cls
    if field_type == FieldDescriptor.TYPE_ENUM:
        return FieldType.enum
    return f'unknown({field_type})'

def dump_class(message_descriptor: Descriptor):
    indent = '   '
    
    # print(f"{indent}Message name: {message_descriptor.name}")
    # print(f"{indent}Full name: {message_descriptor.full_name}")
    # print(f"{indent}Fields: {message_descriptor.fields}")
    # print(f"{indent}Nested types: {message_descriptor.nested_types}")
    # print(f"{indent}Enum types: {message_descriptor.enum_types}")
    # print(f"{indent}Oneofs: {message_descriptor.oneofs}")
    
    for oneof in message_descriptor.oneofs:
        print(f"{indent} --- Oneof name: {oneof.name}")
    def is_optional(field: FieldDescriptor) -> bool:
        return field.label == FieldDescriptor.LABEL_OPTIONAL
    
    for f in message_descriptor.fields:
        field: FieldDescriptor = f
        json_name = field.json_name # type: ignore
        oneof = ''
        if field.containing_oneof:
            oneof = f' -- OneOf=\'{field.containing_oneof.name}\' '
        
        if map_field_type(field.type) == FieldType.cls:
            obj_type = field.message_type.full_name
            print(f"{indent}{oneof}{field.full_name}, name='{json_name}', type='{map_field_type(field.type)} = {obj_type}' ")
            continue
        if (is_optional(field)):
            print(f"{indent}{oneof}{field.full_name}, name='{json_name}', type='Optional[{map_field_type(field.type)}]'")
            continue
        
        print(f"{indent}{oneof}{field.full_name}, name='{json_name}', type='{map_field_type(field.type)}'")
    

def config_testing():
    # Get the module descriptor
    module_descriptor = config_pb2.DESCRIPTOR
    
    doc = ModelGeneratorDoc([
        config_pb2.DESCRIPTOR,
    ])
    

    # List all message types
    for message_type in module_descriptor.message_types_by_name:
        print(f"-- message name: {message_type} -- ")
        dump_class(module_descriptor.message_types_by_name[message_type]) # type: ignore

    # If you want to list nested messages within each top-level message
    # for message_type in module_descriptor.message_types_by_name.values():
    #     print(f"Top-level message name: {message_type.name}")
    #     for nested_type in message_type.nested_types:
    #         print(f"  Nested message name: {nested_type.name}")
    
    
    
    # dump_class(config_pb2.Config) # type: ignore

    # cfg = ModelConfig(id='1')
    # cfg.fooA = ModelFooA(id='2', name='foo-a', type=ValueType.TYPE_A)
    # cfg.fooB = ModelFooB(id='3', enabled=True)

    # x = cfg.clone()

    # data = cfg.to_dict()
    # print(data)

    # json_dict = MessageToDict(cfg)
    # print(json.dumps(json_dict, indent='  '))

    # cfg_copy = ParseDict(json_dict, config_pb2.Config())
    # cfg_copy.id = 'a copy'
    # print(json.dumps(MessageToDict(cfg_copy), indent='  '))

    # fooa = ModelFooA(id='1', value='3', type_optional=ValueType.TYPE_B, type=ValueType.TYPE_B)
    # data = fooa.to_dict()
    # print(data)
    # fooa_copy = ModelFooA.from_dict(data)
    # print(fooa_copy.to_dict())



    pass

if __name__== '__main__':
    config_testing()
    pass