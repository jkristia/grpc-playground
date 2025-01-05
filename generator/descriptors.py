from __future__ import annotations
from enum import Enum
from typing import List, Optional, cast
from google.protobuf.descriptor import FileDescriptor, Descriptor, FieldDescriptor

class FieldType(Enum):
    cls = 'class'
    str = 'str'
    int = 'int'
    float = 'float'
    enum = 'enum'
    bool = 'bool'

def map_field_type(field_type: int) -> FieldType | str:
    if field_type == FieldDescriptor.TYPE_INT32:
        return FieldType.int
    if field_type == FieldDescriptor.TYPE_INT64:
        return FieldType.int
    if field_type == FieldDescriptor.TYPE_BOOL:
        return FieldType.bool
    if field_type == FieldDescriptor.TYPE_FLOAT:
        return FieldType.float
    if field_type == FieldDescriptor.TYPE_STRING:
        return FieldType.str
    if field_type == FieldDescriptor.TYPE_MESSAGE:
        return FieldType.cls
    if field_type == FieldDescriptor.TYPE_ENUM:
        return FieldType.enum
    return f'unknown({field_type})'

class ModelFieldDescriptor():
    @property
    def json_name(self) -> str:
        """ json name return the name as camel case instead of snake_case as defined in .proto"""
        return self.descriptor.json_name # type: ignore
    
    @property
    def name(self) -> str:
        """ the name as defined in the .proto """
        return self.descriptor.name
    
    @property
    def property_type(self) -> FieldType:
        return cast(FieldType, map_field_type(self.descriptor.type))

    @property
    def object_type(self) -> str:
        if self.property_type == FieldType.cls and self.descriptor.message_type is not None:
            return self.doc.model_prefix + self.descriptor.message_type.name
            # return self.descriptor.message_type.full_name
        if self.property_type == FieldType.enum and self.descriptor.enum_type is not None:
            return self.doc.model_prefix + self.descriptor.enum_type.name
            # return self.descriptor.message_type.full_name
        return ''
    
    @property
    def is_optional(self) -> bool:
        # all fields are optional in proto3
        return True # self.descriptor.label == FieldDescriptor.LABEL_OPTIONAL

    @property
    def is_repeated(self) -> bool:
        return self.descriptor.label == FieldDescriptor.LABEL_REPEATED
    
    def __init__(self, doc: ModelGeneratorDoc, descriptor: FieldDescriptor):
        self.descriptor = descriptor
        self.doc = doc

    def __repr__(self) -> str:
        return f'(field) {self.json_name}'


class ModelMessageDescriptor():
    @property
    def name(self) -> str:
        return self.descriptor.name
    
    @property
    def class_name(self) -> str:
        return f'{self.doc.model_prefix}{self.name}'
    
    def __init__(self, doc: ModelGeneratorDoc, descriptor: Descriptor):
        self.descriptor = descriptor
        self.doc: ModelGeneratorDoc = doc
        self.fields: List[ModelFieldDescriptor] = []
        for field in descriptor.fields:
            self.fields.append(ModelFieldDescriptor(self.doc, field))

    def find_field(self, name: str) -> Optional[ModelFieldDescriptor]:
        for field in self.fields:
            if field.json_name == name:
                return field
        return None

    def __repr__(self) -> str:
        return f'(message) {self.descriptor.name}'

class ModelModuleDescriptor():
    @property
    def name(self) -> str:
        return self.descriptor.package
    
    def __init__(self, doc: ModelGeneratorDoc, descriptor: FileDescriptor):
        self.descriptor = descriptor
        self.messages: List[ModelMessageDescriptor] = []
        for message_type in descriptor.message_types_by_name:
            message = self.descriptor.message_types_by_name[message_type]
            self.messages.append(ModelMessageDescriptor(doc, message))
        
    def find_message(self, name: str) -> Optional[ModelMessageDescriptor]:
        for message in self.messages:
            if message.name == name:
                return message
        return None
            
    def __repr__(self) -> str:
        return f'(module) {self.descriptor.name}'

class ModelGeneratorDoc():
    
    @property
    def model_prefix(self) -> str:
        return 'model_'
    def __init__(self, modules: List[FileDescriptor]):
        self.modules: List[ModelModuleDescriptor] = []
        for module in modules:
            self.modules.append(ModelModuleDescriptor(self, module))
    
    def find_module(self, name: str) -> Optional[ModelModuleDescriptor]:
        for module in self.modules:
            if module.name == name:
                return module
        return None
                     
