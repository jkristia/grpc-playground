
from descriptors import ModelGeneratorDoc, ModelMessageDescriptor, FieldType
from string_writer import StringWriter

class ClassWriter():
    
   
    def __init__(self, doc: ModelGeneratorDoc, descriptor: ModelMessageDescriptor):
        self._doc = doc
        self._descriptor = descriptor
        pass
    
    def write(self, wr: StringWriter) -> StringWriter:
        self._write_class(wr)
        self._write_constants(wr)
        self._write_fields(wr)
        self._write_end(wr)
        return wr
    
    def _write_class(self, wr: StringWriter):
        wr.writeln('@dataclass')
        wr.writeln(f'class {self._descriptor.class_name}({self._doc.model_prefix}Base):')
        pass
    
    def _write_constants(self, wr: StringWriter):
        wr.indent()
        wr.writeln('')
        wr.writeln(f'CLASS_NAME = \'{self._descriptor.class_name}\'')
        for field in self._descriptor.fields:
            wr.writeln(f'{field.json_name.upper()} = \'{field.json_name}\'')
            pass
        wr.pop_indent()
            
    def _write_fields(self, wr: StringWriter):
        wr.indent()
        wr.writeln('')
        for field in self._descriptor.fields:
            
            property_type = field.property_type.value
            if field.property_type == FieldType.cls:
                property_type = field.object_type
            if field.property_type == FieldType.enum:
                property_type = field.object_type
            
            type = f'Optional[{property_type}]'
            if (field.is_repeated):
                type = f'Optional[List[{property_type}]]'
            wr.writeln(f'{field.json_name}: {type} = None')
            pass
        wr.pop_indent()
            
    
    def _write_end(self, wr: StringWriter):
        wr.indent().writeln('pass')
        wr.pop_indent()
        wr.writeln('')
        pass
