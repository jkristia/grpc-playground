
from descriptors import ModelGeneratorDoc, ModelMessageDescriptor
from string_writer import StringWriter

class ImportWriter():
    
    def __init__(self, doc: ModelGeneratorDoc):
        self._doc = doc
        pass
    
    def write(self, wr: StringWriter) -> StringWriter:
        wr.writeln(
            'from typing import Optional, List, Any',
            'from dataclasses import dataclass, asdict',
            'from enum import Enum',
        )
        # additional import added to docs will be added here
        return wr
