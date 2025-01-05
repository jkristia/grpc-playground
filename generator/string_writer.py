
from typing import List


class StringWriter():
    indent_char = '\t'

    @property
    def lines(self) -> List[str]:
        return self._lines
    
    def __init__(self):
        self._indent_len = 0
        self._indent: str = ''
        self._lines: List[str] = []
        
    def add(self, writers: List['StringWriter']) -> 'StringWriter':
        for writer in writers:
            self._lines.extend(writer._lines)
        return self
        
    def indent(self) -> 'StringWriter':
        self._indent_len += 1
        self._indent = ''.join([StringWriter.indent_char for _ in range(self._indent_len)])
        return self
    
    def pop_indent(self) -> 'StringWriter':
        self._indent_len -= 1
        if self._indent_len < 0:
            self._indent_len = 0
        self._indent = ''.join([StringWriter.indent_char for _ in range(self._indent_len)])
        return self
    
    def writeln(self, *lines: str) -> 'StringWriter':
        for line in lines:
            self._lines.append(self._indent + line)
        return self
    
    def to_string(self) -> str:
        return '\n'.join(self._lines)
