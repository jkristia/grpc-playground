from baseclass_writer import BaseClassWriter
from class_writer import ClassWriter
from enum_writer import EnumWriter
from generator_test import module_a_pb2, module_b_pb2
from descriptors import FieldType, ModelFieldDescriptor, ModelGeneratorDoc, ModelModuleDescriptor, ModelMessageDescriptor
from import_writer import ImportWriter
from string_writer import StringWriter 


class Generator():
    
    def __init__(self, doc: ModelGeneratorDoc):
        self._doc = doc
    
    def write(self) -> StringWriter:

        enum_wr = StringWriter()
        for module in doc.modules:
            for message in module.enums:
                EnumWriter(doc, message).write(enum_wr)
                
        class_wr = StringWriter()
        for module in doc.modules:
            for message in module.messages:
                ClassWriter(doc, message).write(class_wr)
        
        import_wr = ImportWriter(doc).write(StringWriter())
        base_wr = BaseClassWriter(doc).write(StringWriter())
        return StringWriter().add([import_wr, base_wr, enum_wr, class_wr])
        
        
if __name__ == '__main__':
    doc = ModelGeneratorDoc([
        module_a_pb2.DESCRIPTOR,
        module_b_pb2.DESCRIPTOR
    ])
    generator = Generator(doc)
    wr = generator.write()
    with open('generator/test/model_autogen.py', 'w') as file:
        file.write(wr.to_string())
            
    
    