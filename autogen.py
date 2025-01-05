from typing import Optional, List, Any
from dataclasses import dataclass, asdict
from enum import Enum

@dataclass
class model_Base():
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
        
                   
@dataclass
class model_BasicSubItem(model_Base):
	
	CLASS_NAME = 'model_BasicSubItem'
	NAME = 'name'
	
	name: Optional[str] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'model_BasicSubItem':
		return cls(**data).after_serialize_in()
	
	def clone(self) -> 'model_BasicSubItem':
		return model_BasicSubItem.from_dict(self.to_dict())
	pass
	
@dataclass
class model_BasicMessageA(model_Base):
	
	CLASS_NAME = 'model_BasicMessageA'
	NAME = 'name'
	INTVALUE = 'intValue'
	FLOATVALUE = 'floatValue'
	BOOLVALUE = 'boolValue'
	ENUMVALUE = 'enumValue'
	REPEATEDFIELD = 'repeatedField'
	SUBITEM = 'subItem'
	ONAME = 'oName'
	OINTVALUE = 'oIntValue'
	OFLOATVALUE = 'oFloatValue'
	OBOOLVALUE = 'oBoolValue'
	OENUMVALUE = 'oEnumValue'
	
	name: Optional[str] = None
	intValue: Optional[int] = None
	floatValue: Optional[float] = None
	boolValue: Optional[bool] = None
	enumValue: Optional[model_BasicEnum] = None
	repeatedField: Optional[List[int]] = None
	subItem: Optional[model_BasicSubItem] = None
	oName: Optional[str] = None
	oIntValue: Optional[int] = None
	oFloatValue: Optional[float] = None
	oBoolValue: Optional[bool] = None
	oEnumValue: Optional[model_BasicEnum] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'model_BasicMessageA':
		return cls(**data).after_serialize_in()
	
	def clone(self) -> 'model_BasicMessageA':
		return model_BasicMessageA.from_dict(self.to_dict())
	pass
	
@dataclass
class model_BasicMessageB(model_Base):
	
	CLASS_NAME = 'model_BasicMessageB'
	NAME = 'name'
	
	name: Optional[str] = None
	
	@classmethod
	def from_dict(cls, data: dict) -> 'model_BasicMessageB':
		return cls(**data).after_serialize_in()
	
	def clone(self) -> 'model_BasicMessageB':
		return model_BasicMessageB.from_dict(self.to_dict())
	pass
	