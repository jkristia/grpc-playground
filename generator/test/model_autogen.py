from __future__ import annotations
from google.protobuf.json_format import MessageToDict
from typing import Optional, List, Any, cast
from dataclasses import dataclass, asdict
from enum import Enum
"""
    auto generated file, model classes generated from protobuf classes
    
    example of usage:
    
    from google.protobuf.json_format import MessageToDict
    # proto buf message
    pbMsg = pb2.MyMessage(...)
    # convert to autogenerated Model object
    modelMsg = ModelMyMessage.from_dict(ModelBase.dict_from_pb_message(pbMsg))
"""

MODEL_VERSION = '0.0.1'


@dataclass
class ModelBase():
    def to_dict(self) -> Any:
        return self._to_dict(asdict(self))
    
    def _to_dict(self, obj) -> Any:
        # return enum name, not value
        if isinstance(obj, Enum):
            return obj.name
        # remove None values
        if isinstance(obj, list):
            return [self._to_dict(item) for item in obj if item is not None]
        if isinstance(obj, dict):
            return {key: self._to_dict(value) for key, value in obj.items() if value is not None }
        else:
            return obj
        
    def after_serialize_in(self) -> Any:
        return self
        
    @classmethod
    def dict_from_pb_message(cls, pb_msg: Any) -> dict:
        return MessageToDict(pb_msg, always_print_fields_with_no_presence=True)

                   
class ModelBasicEnum(Enum):
	UNKNOWN = 'UNKNOWN'
	VALUE_1 = 'VALUE_1'
	ABC = 'ABC'
	LOWER_CASE_VALUE = 'lower_case_value'

@dataclass
class ModelBasicSubItem(ModelBase):
	CLASS_NAME = 'ModelBasicSubItem'
	# protobuf names
	PB_NAME = 'name'
	PB_SINGLEPOINT = 'singlePoint'
	# json / dict names
	NAME = 'name'
	SINGLEPOINT = 'singlePoint'
	
	name: Optional[str] = None
	singlePoint: Optional[ModelSomePoint] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'ModelBasicSubItem':
		return cls(**data).after_serialize_in()
	
	@classmethod
	def from_pb_msg(cls, pb_msg: Any) -> 'ModelBasicSubItem':
		data = ModelBase.dict_from_pb_message(pb_msg)
		return cls(**data).after_serialize_in()
                   
	def after_serialize_in(self) -> 'ModelBasicSubItem':
		if self.singlePoint is not None:
			raw: Any = self.singlePoint
			self.singlePoint = ModelSomePoint(**raw).after_serialize_in()
		return self
	
	def clone(self) -> 'ModelBasicSubItem':
		return ModelBasicSubItem.from_dict(self.to_dict())
	pass
	
@dataclass
class ModelSomePoint(ModelBase):
	CLASS_NAME = 'ModelSomePoint'
	# protobuf names
	PB_X = 'x'
	PB_Y = 'y'
	# json / dict names
	X = 'x'
	Y = 'y'
	
	x: Optional[float] = None
	y: Optional[float] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'ModelSomePoint':
		return cls(**data).after_serialize_in()
	
	@classmethod
	def from_pb_msg(cls, pb_msg: Any) -> 'ModelSomePoint':
		data = ModelBase.dict_from_pb_message(pb_msg)
		return cls(**data).after_serialize_in()
                   
	def after_serialize_in(self) -> 'ModelSomePoint':
		return self
	
	def clone(self) -> 'ModelSomePoint':
		return ModelSomePoint.from_dict(self.to_dict())
	pass
	
@dataclass
class ModelBasicMessageA(ModelBase):
	CLASS_NAME = 'ModelBasicMessageA'
	# protobuf names
	PB_NAME = 'name'
	PB_INT_VALUE = 'int_value'
	PB_FLOAT_VALUE = 'float_value'
	PB_BOOL_VALUE = 'bool_value'
	PB_ENUM_VALUE = 'enum_value'
	PB_REPEATED_FIELD = 'repeated_field'
	PB_SUB_ITEM = 'sub_item'
	PB_O_NAME = 'o_name'
	PB_O_INT_VALUE = 'o_int_value'
	PB_O_FLOAT_VALUE = 'o_float_value'
	PB_O_BOOL_VALUE = 'o_bool_value'
	PB_O_ENUM_VALUE = 'o_enum_value'
	# json / dict names
	NAME = 'name'
	INT_VALUE = 'intValue'
	FLOAT_VALUE = 'floatValue'
	BOOL_VALUE = 'boolValue'
	ENUM_VALUE = 'enumValue'
	REPEATED_FIELD = 'repeatedField'
	SUB_ITEM = 'subItem'
	O_NAME = 'oName'
	O_INT_VALUE = 'oIntValue'
	O_FLOAT_VALUE = 'oFloatValue'
	O_BOOL_VALUE = 'oBoolValue'
	O_ENUM_VALUE = 'oEnumValue'
	
	name: Optional[str] = None
	intValue: Optional[int] = None
	floatValue: Optional[float] = None
	boolValue: Optional[bool] = None
	enumValue: Optional[ModelBasicEnum] = None
	repeatedField: Optional[List[int]] = None
	subItem: Optional[ModelBasicSubItem] = None
	oName: Optional[str] = None
	oIntValue: Optional[int] = None
	oFloatValue: Optional[float] = None
	oBoolValue: Optional[bool] = None
	oEnumValue: Optional[ModelBasicEnum] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'ModelBasicMessageA':
		return cls(**data).after_serialize_in()
	
	@classmethod
	def from_pb_msg(cls, pb_msg: Any) -> 'ModelBasicMessageA':
		data = ModelBase.dict_from_pb_message(pb_msg)
		return cls(**data).after_serialize_in()
                   
	def after_serialize_in(self) -> 'ModelBasicMessageA':
		if self.enumValue is not None:
			self.enumValue = ModelBasicEnum(self.enumValue)
		if self.oEnumValue is not None:
			self.oEnumValue = ModelBasicEnum(self.oEnumValue)
		if self.subItem is not None:
			raw: Any = self.subItem
			self.subItem = ModelBasicSubItem(**raw).after_serialize_in()
		return self
	
	def clone(self) -> 'ModelBasicMessageA':
		return ModelBasicMessageA.from_dict(self.to_dict())
	pass
	
@dataclass
class ModelMsgWithRepeatedProps(ModelBase):
	CLASS_NAME = 'ModelMsgWithRepeatedProps'
	# protobuf names
	PB_TXT = 'txt'
	PB_LINES = 'lines'
	PB_ENUMS = 'enums'
	PB_POINTS = 'points'
	# json / dict names
	TXT = 'txt'
	LINES = 'lines'
	ENUMS = 'enums'
	POINTS = 'points'
	
	txt: Optional[str] = None
	lines: Optional[List[str]] = None
	enums: Optional[List[ModelBasicEnum]] = None
	points: Optional[List[ModelSomePoint]] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'ModelMsgWithRepeatedProps':
		return cls(**data).after_serialize_in()
	
	@classmethod
	def from_pb_msg(cls, pb_msg: Any) -> 'ModelMsgWithRepeatedProps':
		data = ModelBase.dict_from_pb_message(pb_msg)
		return cls(**data).after_serialize_in()
                   
	def after_serialize_in(self) -> 'ModelMsgWithRepeatedProps':
		if self.enums is not None:
			values = cast(List[str], self.enums) 
			self.enums = [ModelBasicEnum(value) for value in values]
		if self.points is not None:
			values = cast(List[Any], self.points) 
			self.points = [ModelSomePoint(**value).after_serialize_in() for value in values]
		return self
	
	def clone(self) -> 'ModelMsgWithRepeatedProps':
		return ModelMsgWithRepeatedProps.from_dict(self.to_dict())
	pass
	
@dataclass
class ModelBasicMessageB(ModelBase):
	CLASS_NAME = 'ModelBasicMessageB'
	# protobuf names
	PB_NAME = 'name'
	# json / dict names
	NAME = 'name'
	
	name: Optional[str] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'ModelBasicMessageB':
		return cls(**data).after_serialize_in()
	
	@classmethod
	def from_pb_msg(cls, pb_msg: Any) -> 'ModelBasicMessageB':
		data = ModelBase.dict_from_pb_message(pb_msg)
		return cls(**data).after_serialize_in()
                   
	def after_serialize_in(self) -> 'ModelBasicMessageB':
		return self
	
	def clone(self) -> 'ModelBasicMessageB':
		return ModelBasicMessageB.from_dict(self.to_dict())
	pass
	