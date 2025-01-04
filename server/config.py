from typing import Optional, Union, Any, get_origin, get_args, ClassVar
from dataclasses import dataclass, asdict
from enum import Enum
from google.protobuf.json_format import MessageToJson, MessageToDict, ParseDict
# from config_pb2 import Config, FooA, FooB
import config_pb2
import json

class ValueType(Enum):
    UNKNOWN = 'UNKNOWN'
    TYPE_A = 'TYPE_A'
    TYPE_B = 'TYPE_B'

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


@dataclass
class ModelFooA(ModelBase):
    id: str
    type: ValueType
    name: Optional[str] = None
    value: Optional[int] = None
    type_optional: Optional[ValueType] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ModelFooA':
        return cls(**data).after_serialize_in()

    def after_serialize_in(self) -> 'ModelFooA':
        if self.type is not None:
            self.type = ValueType(self.type)
        if self.type_optional is not None:
            self.type_optional = ValueType(self.type_optional)
        return self

    def clone(self) -> 'ModelFooA':
        return ModelFooA.from_dict(self.to_dict())



@dataclass
class ModelFooB(ModelBase):
    id: str
    enabled: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> 'ModelFooB':
        return cls(**data).after_serialize_in()

    def after_serialize_in(self) -> 'ModelFooB':
        return self

    def clone(self) -> 'ModelFooB':
        return ModelFooB.from_dict(self.to_dict())

@dataclass
class ModelConfig(ModelBase):
    
    id: str
    fooA: Optional[ModelFooA] = None
    fooB: Optional[ModelFooB] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ModelConfig':
        return cls(**data).after_serialize_in()

    def after_serialize_in(self) -> 'ModelConfig':
        if self.fooA is not None:
            raw: Any = self.fooA
            self.fooA = ModelFooA(**raw).after_serialize_in()
        if self.fooB is not None:
            raw: Any = self.fooB
            self.fooB = ModelFooB(**raw).after_serialize_in()
            
        return self

    def clone(self) -> 'ModelConfig':
        return ModelConfig.from_dict(self.to_dict())


def config_testing():

    cfg = ModelConfig(id='1')
    cfg.fooA = ModelFooA(id='2', name='foo-a', type=ValueType.TYPE_A)
    cfg.fooB = ModelFooB(id='3', enabled=True)

    x = cfg.clone()

    data = cfg.to_dict()
    print(data)


    # json_dict = MessageToDict(cfg)
    # print(json.dumps(json_dict, indent='  '))

    # cfg_copy = ParseDict(json_dict, config_pb2.Config())
    # cfg_copy.id = 'a copy'
    # print(json.dumps(MessageToDict(cfg_copy), indent='  '))

    # fooa = ModelFooA(id='1', value='3', type_optional=ValueType.TYPE_B, type=ValueType.TYPE_B)
    # data = fooa.to_dict()
    # print(data)
    # fooa_copy = ModelFooA.from_dict(data)
    # print(fooa_copy.to_dict())



    pass

if __name__== '__main__':
    config_testing()
    pass