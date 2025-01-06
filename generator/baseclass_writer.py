
from descriptors import ModelGeneratorDoc, ModelMessageDescriptor
from string_writer import StringWriter

class BaseClassWriter():
	
	def __init__(self, doc: ModelGeneratorDoc):
		self._doc = doc
		pass
	
	def write(self, wr: StringWriter) -> StringWriter:
		self._write_baseclass(wr)
		self._write_titmestamp(wr)
		return wr
	
	def _write_baseclass(self, wr:StringWriter) -> StringWriter:
		wr.writeln(f"""
class {self._doc.baseclass_name}():
	def to_dict(self) -> Any:
		properties = [name for name, value in inspect.getmembers(self.__class__, inspect.isdatadescriptor)]
		d = {{}}
		for property in properties:
			if property.startswith('__'):
				continue
			d[property] = getattr(self, property)
		return self._to_dict(d)
	
	def _to_dict(self, obj) -> Any:
		# return enum name, not value
		if isinstance(obj, Enum):
			return obj.name
		if isinstance(obj, ModelBase) and obj != self:
			return obj.to_dict()
		# remove None values
		if isinstance(obj, list):
			return [self._to_dict(item) for item in obj if item is not None]
		if isinstance(obj, dict):
			return {{key: self._to_dict(value) for key, value in obj.items() if value is not None }}
		if isinstance(obj, Google_Timestamp) and obj != self:
			return obj.time
		else:
			return obj
		
	def after_serialize_in(self) -> Any:
		return self
		
	@classmethod
	def dict_from_pb_message(cls, pb_msg: Any) -> dict:
		return MessageToDict(pb_msg, always_print_fields_with_no_presence=True)

""")
		return wr

	def _write_titmestamp(self, wr:StringWriter) -> StringWriter:
		wr.writeln(f"""
class Google_Timestamp():

	def __init__(self, time: str):
		self.time: str = time
	
""")
		return wr
