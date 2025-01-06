from descriptors import ModelFieldDescriptor, ModelGeneratorDoc, ModelMessageDescriptor, FieldType
from string_writer import StringWriter

class FieldWriter():
   
    @property
    def property_type(self) -> str:
        field = self._field_descriptor
        property_type = field.property_type.value
        if field.property_type == FieldType.cls:
            property_type = field.object_type
        if field.property_type == FieldType.enum:
            property_type = field.object_type
            
        type = f'Optional[{property_type}]'
        if (field.is_repeated):
            type = f'Optional[List[{property_type}]]'
        return type
        
    def __init__(self, doc: ModelGeneratorDoc, descriptor: ModelMessageDescriptor, field_descriptor: ModelFieldDescriptor):
        self._doc = doc
        self._descriptor = descriptor
        self._field_descriptor = field_descriptor
        pass
    
    def write(self, wr: StringWriter) -> StringWriter:
        self._write_field(wr)
        return wr
    
    def write_constructor_field(self, wr: StringWriter):
        field = self._field_descriptor
        wr.writeln(f'{field.json_name}: {self.property_type} = None,')
    
    def _write_field(self, wr: StringWriter):
        field = self._field_descriptor
        type = self.property_type
        
        wr.writeln(f'# property {field.json_name}')
        wr.writeln(f'@property')
        wr.writeln(f'def {field.json_name}(self) -> {type}:')
        wr.indent().writeln(f'return self._{field.json_name}').pop_indent()
        wr.writeln(f'@{field.json_name}.setter')
        wr.writeln(f'def {field.json_name}(self, value: {type}):')
        wr.indent()
        oneof_fields = field.one_of_fields
        if len(oneof_fields) > 0:
            for oneof_jsonname in oneof_fields:
                if oneof_jsonname == field.json_name:
                    wr.writeln(f'self._{oneof_jsonname} = value')
                else:
                    wr.writeln(f'self._{oneof_jsonname} = None')
        else:
            wr.writeln(f'self._{field.json_name} = value')
        wr.pop_indent()
        wr.writeln('')
        pass
