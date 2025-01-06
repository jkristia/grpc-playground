
from descriptors import ModelGeneratorDoc, ModelMessageDescriptor
from string_writer import StringWriter

class ImportWriter():
    
    def __init__(self, doc: ModelGeneratorDoc):
        self._doc = doc
        pass
    
    def write(self, wr: StringWriter) -> StringWriter:
        wr.writeln(
            'from __future__ import annotations', # use forward delcare as the order of definitions is not guarenteed
            'from google.protobuf.json_format import MessageToDict',
            'from typing import Optional, List, Any, cast',
            'import inspect',
            'from enum import Enum',
        )
        # additional import added to docs will be added here
        self._write_header(wr)
        self._write_model_version(wr)
        return wr

    header = """
    auto generated file, model classes generated from protobuf classes
    
    example of usage:
    
    from google.protobuf.json_format import MessageToDict
    # proto buf message
    pbMsg = pb2.MyMessage(...)
    # convert to autogenerated Model object
    modelMsg = ModelMyMessage.from_pb_msg(pbMsg)"""


    def _write_header(self, wr: StringWriter):
        wr.writeln('"""' + self.header)
        wr.writeln('"""')

    def _write_model_version(self, wr: StringWriter):
        wr.writeln('')
        wr.writeln(f'MODEL_VERSION = \'{self._doc.model_version}\'')
        wr.writeln('')
