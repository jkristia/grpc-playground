
from descriptors import ModelGeneratorDoc, ModelEnumDescriptor
from field_writer import FieldWriter
from string_writer import StringWriter

class EnumWriter():
   
    def __init__(self, doc: ModelGeneratorDoc, descriptor: ModelEnumDescriptor):
        self._doc = doc
        self._descriptor = descriptor
        pass
    
    def write(self, wr: StringWriter) -> StringWriter:
        wr.writeln(f'### enum: {self._descriptor.descriptor.full_name}')
        wr.writeln(f'class {self._descriptor.class_name}(Enum):')
        wr.indent()
        for value in self._descriptor.values:
            wr.writeln(f'{value.upper()} = \'{value}\'')
        wr.pop_indent()
        wr.writeln('')
        return wr
