from __future__ import annotations
from google.protobuf.json_format import MessageToDict
from typing import Optional, List, Any, cast
import inspect
from enum import Enum
"""
    auto generated file, model classes generated from protobuf classes
    
    example of usage:
    
    from google.protobuf.json_format import MessageToDict
    # proto buf message
    pbMsg = pb2.MyMessage(...)
    # convert to autogenerated Model object
    modelMsg = ModelMyMessage.from_pb_msg(pbMsg)
"""

MODEL_VERSION = '0.0.1'


class ModelBase():
	def to_dict(self) -> Any:
		properties = [name for name, value in inspect.getmembers(self.__class__, inspect.isdatadescriptor)]
		d = {}
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

class ModelBasicSubItem(ModelBase):
	CLASS_NAME = 'ModelBasicSubItem'
	
	# protobuf names
	PB_NAME = 'name'
	PB_SINGLEPOINT = 'singlePoint'
	
	# json / dict names
	NAME = 'name'
	SINGLEPOINT = 'singlePoint'
	
	# property name
	@property
	def name(self) -> Optional[str]:
		return self._name
	@name.setter
	def name(self, value: Optional[str]):
		self._name = value
	
	# property singlePoint
	@property
	def singlePoint(self) -> Optional[ModelSomePoint]:
		return self._singlePoint
	@singlePoint.setter
	def singlePoint(self, value: Optional[ModelSomePoint]):
		self._singlePoint = value
	
	# constructor - ModelBasicSubItem
	def __init__(self,
			name: Optional[str] = None,
			singlePoint: Optional[ModelSomePoint] = None,
			):
		self._name = name
		self._singlePoint = singlePoint
		pass
	
	# serialization
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
	
class ModelSomePoint(ModelBase):
	CLASS_NAME = 'ModelSomePoint'
	
	# protobuf names
	PB_X = 'x'
	PB_Y = 'y'
	
	# json / dict names
	X = 'x'
	Y = 'y'
	
	# property x
	@property
	def x(self) -> Optional[float]:
		return self._x
	@x.setter
	def x(self, value: Optional[float]):
		self._x = value
	
	# property y
	@property
	def y(self) -> Optional[float]:
		return self._y
	@y.setter
	def y(self, value: Optional[float]):
		self._y = value
	
	# constructor - ModelSomePoint
	def __init__(self,
			x: Optional[float] = None,
			y: Optional[float] = None,
			):
		self._x = x
		self._y = y
		pass
	
	# serialization
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
	
	# property name
	@property
	def name(self) -> Optional[str]:
		return self._name
	@name.setter
	def name(self, value: Optional[str]):
		self._name = value
	
	# property intValue
	@property
	def intValue(self) -> Optional[int]:
		return self._intValue
	@intValue.setter
	def intValue(self, value: Optional[int]):
		self._intValue = value
	
	# property floatValue
	@property
	def floatValue(self) -> Optional[float]:
		return self._floatValue
	@floatValue.setter
	def floatValue(self, value: Optional[float]):
		self._floatValue = value
	
	# property boolValue
	@property
	def boolValue(self) -> Optional[bool]:
		return self._boolValue
	@boolValue.setter
	def boolValue(self, value: Optional[bool]):
		self._boolValue = value
	
	# property enumValue
	@property
	def enumValue(self) -> Optional[ModelBasicEnum]:
		return self._enumValue
	@enumValue.setter
	def enumValue(self, value: Optional[ModelBasicEnum]):
		self._enumValue = value
	
	# property repeatedField
	@property
	def repeatedField(self) -> Optional[List[int]]:
		return self._repeatedField
	@repeatedField.setter
	def repeatedField(self, value: Optional[List[int]]):
		self._repeatedField = value
	
	# property subItem
	@property
	def subItem(self) -> Optional[ModelBasicSubItem]:
		return self._subItem
	@subItem.setter
	def subItem(self, value: Optional[ModelBasicSubItem]):
		self._subItem = value
	
	# property oName
	@property
	def oName(self) -> Optional[str]:
		return self._oName
	@oName.setter
	def oName(self, value: Optional[str]):
		self._oName = value
	
	# property oIntValue
	@property
	def oIntValue(self) -> Optional[int]:
		return self._oIntValue
	@oIntValue.setter
	def oIntValue(self, value: Optional[int]):
		self._oIntValue = value
	
	# property oFloatValue
	@property
	def oFloatValue(self) -> Optional[float]:
		return self._oFloatValue
	@oFloatValue.setter
	def oFloatValue(self, value: Optional[float]):
		self._oFloatValue = value
	
	# property oBoolValue
	@property
	def oBoolValue(self) -> Optional[bool]:
		return self._oBoolValue
	@oBoolValue.setter
	def oBoolValue(self, value: Optional[bool]):
		self._oBoolValue = value
	
	# property oEnumValue
	@property
	def oEnumValue(self) -> Optional[ModelBasicEnum]:
		return self._oEnumValue
	@oEnumValue.setter
	def oEnumValue(self, value: Optional[ModelBasicEnum]):
		self._oEnumValue = value
	
	# constructor - ModelBasicMessageA
	def __init__(self,
			name: Optional[str] = None,
			intValue: Optional[int] = None,
			floatValue: Optional[float] = None,
			boolValue: Optional[bool] = None,
			enumValue: Optional[ModelBasicEnum] = None,
			repeatedField: Optional[List[int]] = None,
			subItem: Optional[ModelBasicSubItem] = None,
			oName: Optional[str] = None,
			oIntValue: Optional[int] = None,
			oFloatValue: Optional[float] = None,
			oBoolValue: Optional[bool] = None,
			oEnumValue: Optional[ModelBasicEnum] = None,
			):
		self._name = name
		self._intValue = intValue
		self._floatValue = floatValue
		self._boolValue = boolValue
		self._enumValue = enumValue
		self._repeatedField = repeatedField
		self._subItem = subItem
		self._oName = oName
		self._oIntValue = oIntValue
		self._oFloatValue = oFloatValue
		self._oBoolValue = oBoolValue
		self._oEnumValue = oEnumValue
		pass
	
	# serialization
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
	
	# property txt
	@property
	def txt(self) -> Optional[str]:
		return self._txt
	@txt.setter
	def txt(self, value: Optional[str]):
		self._txt = value
	
	# property lines
	@property
	def lines(self) -> Optional[List[str]]:
		return self._lines
	@lines.setter
	def lines(self, value: Optional[List[str]]):
		self._lines = value
	
	# property enums
	@property
	def enums(self) -> Optional[List[ModelBasicEnum]]:
		return self._enums
	@enums.setter
	def enums(self, value: Optional[List[ModelBasicEnum]]):
		self._enums = value
	
	# property points
	@property
	def points(self) -> Optional[List[ModelSomePoint]]:
		return self._points
	@points.setter
	def points(self, value: Optional[List[ModelSomePoint]]):
		self._points = value
	
	# constructor - ModelMsgWithRepeatedProps
	def __init__(self,
			txt: Optional[str] = None,
			lines: Optional[List[str]] = None,
			enums: Optional[List[ModelBasicEnum]] = None,
			points: Optional[List[ModelSomePoint]] = None,
			):
		self._txt = txt
		self._lines = lines
		self._enums = enums
		self._points = points
		pass
	
	# serialization
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
	
class ModelMsgWithOneOfProps(ModelBase):
	CLASS_NAME = 'ModelMsgWithOneOfProps'
	
	# protobuf names
	PB_TXT = 'txt'
	PB_POINT_A = 'point_a'
	PB_POINT_B = 'point_b'
	
	# json / dict names
	TXT = 'txt'
	POINT_A = 'pointA'
	POINT_B = 'pointB'
	
	# property txt
	@property
	def txt(self) -> Optional[str]:
		return self._txt
	@txt.setter
	def txt(self, value: Optional[str]):
		self._txt = value
	
	# property pointA
	@property
	def pointA(self) -> Optional[ModelSomePoint]:
		return self._pointA
	@pointA.setter
	def pointA(self, value: Optional[ModelSomePoint]):
		self._pointA = value
		self._pointB = None
	
	# property pointB
	@property
	def pointB(self) -> Optional[ModelSomePoint]:
		return self._pointB
	@pointB.setter
	def pointB(self, value: Optional[ModelSomePoint]):
		self._pointA = None
		self._pointB = value
	
	# constructor - ModelMsgWithOneOfProps
	def __init__(self,
			txt: Optional[str] = None,
			pointA: Optional[ModelSomePoint] = None,
			pointB: Optional[ModelSomePoint] = None,
			):
		self._txt = txt
		self._pointA = pointA
		self._pointB = pointB
		pass
	
	# serialization
	@classmethod
	def from_dict(cls, data: dict) -> 'ModelMsgWithOneOfProps':
		return cls(**data).after_serialize_in()
	
	@classmethod
	def from_pb_msg(cls, pb_msg: Any) -> 'ModelMsgWithOneOfProps':
		data = ModelBase.dict_from_pb_message(pb_msg)
		return cls(**data).after_serialize_in()
				   
	def after_serialize_in(self) -> 'ModelMsgWithOneOfProps':
		if self.pointA is not None:
			raw: Any = self.pointA
			self.pointA = ModelSomePoint(**raw).after_serialize_in()
		if self.pointB is not None:
			raw: Any = self.pointB
			self.pointB = ModelSomePoint(**raw).after_serialize_in()
		return self
	
	def clone(self) -> 'ModelMsgWithOneOfProps':
		return ModelMsgWithOneOfProps.from_dict(self.to_dict())
	pass
	
class ModelBasicMessageB(ModelBase):
	CLASS_NAME = 'ModelBasicMessageB'
	
	# protobuf names
	PB_NAME = 'name'
	
	# json / dict names
	NAME = 'name'
	
	# property name
	@property
	def name(self) -> Optional[str]:
		return self._name
	@name.setter
	def name(self, value: Optional[str]):
		self._name = value
	
	# constructor - ModelBasicMessageB
	def __init__(self,
			name: Optional[str] = None,
			):
		self._name = name
		pass
	
	# serialization
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
	