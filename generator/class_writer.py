
from descriptors import ModelFieldDescriptor, ModelGeneratorDoc, ModelMessageDescriptor, FieldType
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
		self._write_constructor(wr)
		self._write_serialization(wr)
		self._write_end(wr)
		wr.pop_indent()
		return wr
	
	def _write_class(self, wr: StringWriter):
		wr.writeln(f'### message: {self._descriptor.descriptor.full_name}')
		wr.writeln(f'class {self._descriptor.class_name}({self._doc.baseclass_name}):')
		pass
	
	def _write_constructor(self, wr: StringWriter):
		wr.writeln(f'# constructor - {self._descriptor.class_name}')
		wr.writeln('def __init__(self,')
		wr.indent().indent()
		for field in self._descriptor.fields:
			fieldwriter = FieldWriter(self._doc, self._descriptor, field)
			fieldwriter.write_constructor_field(wr)
		wr.writeln('):')
		wr.pop_indent()
		for field in self._descriptor.fields:
			wr.writeln(f'self._{field.json_name} = {field.json_name}')
		wr.pop_indent()
		
		wr.indent().writeln('pass').pop_indent()
		
	
	def _write_constants(self, wr: StringWriter):
		wr.writeln(f'CLASS_NAME = \'{self._descriptor.class_name}\'')
		wr.writeln('','# protobuf names')
		for field in self._descriptor.fields:
			wr.writeln(f'PB_{field.name.upper()} = \'{field.name}\'')
		wr.writeln('','# json / dict names')
		for field in self._descriptor.fields:
			wr.writeln(f'{field.name.upper()} = \'{field.json_name}\'')
		wr.writeln('')
		pass
			
	def _write_fields(self, wr: StringWriter):
		for field in self._descriptor.fields:
			FieldWriter(self._doc, self._descriptor, field).write(wr)
			
	def _write_serialization(self, wr: StringWriter):
		name = self._descriptor.class_name
		wr.writeln(f"""
	# serialization
	@classmethod
	def from_dict(cls, data: dict) -> '{name}':
		return cls(**data).after_serialize_in()""")
		wr.writeln(f"""
	@classmethod
	def from_pb_msg(cls, pb_msg: Any) -> '{name}':
		data = ModelBase.dict_from_pb_message(pb_msg)
		return cls(**data).after_serialize_in()
				   """)
		self._write_after_serialize_in(wr)
		wr.writeln('')
		wr.writeln(f'def clone(self) -> \'{name}\':')
		wr.indent().writeln(f'return {name}.from_dict(self.to_dict())')
		wr.pop_indent()
		
	def _write_after_serialize_in(self, wr: StringWriter):
		wr.writeln(f'def after_serialize_in(self) -> \'{self._descriptor.class_name}\':')
		wr.indent()
		# handle enums, convert from string value to enum type
		fields = [field for field in self._descriptor.fields if field.property_type == FieldType.enum]
		for field in fields:
			wr.writeln(f'if self.{field.json_name} is not None:').indent()
			if field.is_repeated:
				wr.writeln(f'values = cast(List[str], self.{field.json_name}) ')
				wr.writeln(f'self.{field.json_name} = [{field.object_type}(value) for value in values]').pop_indent()
			else:
				wr.writeln(f'self.{field.json_name} = {field.object_type}(self.{field.json_name})').pop_indent()
		
		# instantiate child objects, what is serialized in the a dict
		fields = [field for field in self._descriptor.fields if field.property_type == FieldType.cls]
		for field in fields:
			wr.writeln(f'if self.{field.json_name} is not None:').indent()
			if field.is_map:
				self._write_map_initialize(wr, field)
				continue
			if field.is_repeated:
				wr.writeln(f'values = cast(List[Any], self.{field.json_name}) ')
				wr.writeln(f'self.{field.json_name} = [{field.object_type}(**value).after_serialize_in() for value in values]').pop_indent()
			else:
				wr.writeln(f'raw: Any = self.{field.json_name}')
				wr.writeln(f'self.{field.json_name} = {field.object_type}(**raw).after_serialize_in()').pop_indent()

		wr.writeln('return self')
		wr.pop_indent()

	def _write_map_initialize(self, wr: StringWriter, field: ModelFieldDescriptor):
		if field.is_map_value_type_class:
			wr.writeln('newmap = {}')
			wr.writeln(f'for key, value in self.{field.json_name}.items():').indent()
			wr.writeln('raw: Any = value')
			wr.writeln(f'newmap[key] = {field.map_value_type}(**raw).after_serialize_in()')
			wr.pop_indent()
			wr.writeln(f'self.{field.json_name} = newmap')
			wr.pop_indent()
			return
		wr.writeln('pass').pop_indent()
		pass
		
	def _write_end(self, wr: StringWriter):
		wr.writeln('pass')
		wr.writeln('')
		pass
