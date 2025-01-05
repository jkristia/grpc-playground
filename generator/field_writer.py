
from descriptors import ModelFieldDescriptor, ModelGeneratorDoc, ModelMessageDescriptor, FieldType
from string_writer import StringWriter

class FieldWriter():
   
    def __init__(self, doc: ModelGeneratorDoc, descriptor: ModelMessageDescriptor, field_descriptor: ModelFieldDescriptor):
        self._doc = doc
        self._descriptor = descriptor
        self._field_descriptor = field_descriptor
        pass
    
    def write(self, wr: StringWriter) -> StringWriter:
        self._write_field(wr)
        return wr
    
    def _write_field(self, wr: StringWriter):
        field = self._field_descriptor
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
