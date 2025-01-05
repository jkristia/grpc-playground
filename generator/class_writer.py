
from descriptors import ModelGeneratorDoc, ModelMessageDescriptor, FieldType
from field_writer import FieldWriter
from string_writer import StringWriter

class ClassWriter():
   
    def __init__(self, doc: ModelGeneratorDoc, descriptor: ModelMessageDescriptor):
        self._doc = doc
        self._descriptor = descriptor
        pass
    
    def write(self, wr: StringWriter) -> StringWriter:
        self._write_class(wr)
        wr.indent()
        self._write_constants(wr)
        self._write_fields(wr)
        self._write_serialization(wr)
        self._write_end(wr)
        wr.pop_indent()
        return wr
    
    def _write_class(self, wr: StringWriter):
        wr.writeln('@dataclass')
        wr.writeln(f'class {self._descriptor.class_name}({self._doc.model_prefix}Base):')
        pass
    
    def _write_constants(self, wr: StringWriter):
        wr.writeln('')
        wr.writeln(f'CLASS_NAME = \'{self._descriptor.class_name}\'')
        for field in self._descriptor.fields:
            wr.writeln(f'{field.json_name.upper()} = \'{field.json_name}\'')
            pass
            
    def _write_fields(self, wr: StringWriter):
        wr.writeln('')
        for field in self._descriptor.fields:
            FieldWriter(self._doc, self._descriptor, field).write(wr)
            
    def _write_serialization(self, wr: StringWriter):
        name = self._descriptor.class_name
        wr.writeln('')
        wr.writeln('@classmethod')
        wr.writeln(f'def from_dict(cls, data: dict) -> \'{name}\':')
        wr.indent().writeln('return cls(**data).after_serialize_in()')
        wr.pop_indent()
        self._write_after_serialize_in(wr)
        wr.writeln('')
        wr.writeln(f'def clone(self) -> \'{name}\':')
        wr.indent().writeln(f'return {name}.from_dict(self.to_dict())')
        wr.pop_indent()
        
    def _write_after_serialize_in(self, wr: StringWriter):
        wr.writeln('')
        wr.writeln(f'def after_serialize_in(self) -> \'{self._descriptor.class_name}\':')
        wr.indent()
        # handle enums, convert from string value to enum type
        fields = [field for field in self._descriptor.fields if field.property_type == FieldType.enum]
        for field in fields:
            wr.writeln(f'if self.{field.name} is not None:').indent()
            wr.writeln(f'self.{field.name} = {field.object_type}(self.{field.name})').pop_indent()
        
        # instantiate child objects, what is serialized in the a dict
        fields = [field for field in self._descriptor.fields if field.property_type == FieldType.cls]
        for field in fields:
            wr.writeln(f'if self.{field.name} is not None:').indent()
            wr.writeln(f'raw: Any = self.{field.name}')
            wr.writeln(f'self.{field.name} = {field.object_type}(**raw).after_serialize_in()').pop_indent()

        wr.writeln('return self')
        wr.pop_indent()
        
    def _write_end(self, wr: StringWriter):
        wr.writeln('pass')
        wr.writeln('')
        pass
