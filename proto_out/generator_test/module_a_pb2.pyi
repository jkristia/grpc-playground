"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _BasicEnum:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _BasicEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BasicEnum.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _BasicEnum.ValueType  # 0
    VALUE_1: _BasicEnum.ValueType  # 1
    ABC: _BasicEnum.ValueType  # 2
    lower_case_value: _BasicEnum.ValueType  # 10

class BasicEnum(_BasicEnum, metaclass=_BasicEnumEnumTypeWrapper): ...

UNKNOWN: BasicEnum.ValueType  # 0
VALUE_1: BasicEnum.ValueType  # 1
ABC: BasicEnum.ValueType  # 2
lower_case_value: BasicEnum.ValueType  # 10
global___BasicEnum = BasicEnum

@typing.final
class BasicSubItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    SINGLEPOINT_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def singlePoint(self) -> global___SomePoint: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        singlePoint: global___SomePoint | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["singlePoint", b"singlePoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "singlePoint", b"singlePoint"]) -> None: ...

global___BasicSubItem = BasicSubItem

@typing.final
class SomePoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float = ...,
        y: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["x", b"x", "y", b"y"]) -> None: ...

global___SomePoint = SomePoint

@typing.final
class BasicMessageA(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    INT_VALUE_FIELD_NUMBER: builtins.int
    FLOAT_VALUE_FIELD_NUMBER: builtins.int
    BOOL_VALUE_FIELD_NUMBER: builtins.int
    ENUM_VALUE_FIELD_NUMBER: builtins.int
    REPEATED_FIELD_FIELD_NUMBER: builtins.int
    SUB_ITEM_FIELD_NUMBER: builtins.int
    O_NAME_FIELD_NUMBER: builtins.int
    O_INT_VALUE_FIELD_NUMBER: builtins.int
    O_FLOAT_VALUE_FIELD_NUMBER: builtins.int
    O_BOOL_VALUE_FIELD_NUMBER: builtins.int
    O_ENUM_VALUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    int_value: builtins.int
    float_value: builtins.float
    bool_value: builtins.bool
    enum_value: global___BasicEnum.ValueType
    o_name: builtins.str
    o_int_value: builtins.int
    o_float_value: builtins.float
    o_bool_value: builtins.bool
    o_enum_value: global___BasicEnum.ValueType
    @property
    def repeated_field(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def sub_item(self) -> global___BasicSubItem: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        int_value: builtins.int = ...,
        float_value: builtins.float = ...,
        bool_value: builtins.bool = ...,
        enum_value: global___BasicEnum.ValueType = ...,
        repeated_field: collections.abc.Iterable[builtins.int] | None = ...,
        sub_item: global___BasicSubItem | None = ...,
        o_name: builtins.str | None = ...,
        o_int_value: builtins.int | None = ...,
        o_float_value: builtins.float | None = ...,
        o_bool_value: builtins.bool | None = ...,
        o_enum_value: global___BasicEnum.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_o_bool_value", b"_o_bool_value", "_o_enum_value", b"_o_enum_value", "_o_float_value", b"_o_float_value", "_o_int_value", b"_o_int_value", "_o_name", b"_o_name", "o_bool_value", b"o_bool_value", "o_enum_value", b"o_enum_value", "o_float_value", b"o_float_value", "o_int_value", b"o_int_value", "o_name", b"o_name", "sub_item", b"sub_item"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_o_bool_value", b"_o_bool_value", "_o_enum_value", b"_o_enum_value", "_o_float_value", b"_o_float_value", "_o_int_value", b"_o_int_value", "_o_name", b"_o_name", "bool_value", b"bool_value", "enum_value", b"enum_value", "float_value", b"float_value", "int_value", b"int_value", "name", b"name", "o_bool_value", b"o_bool_value", "o_enum_value", b"o_enum_value", "o_float_value", b"o_float_value", "o_int_value", b"o_int_value", "o_name", b"o_name", "repeated_field", b"repeated_field", "sub_item", b"sub_item"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_o_bool_value", b"_o_bool_value"]) -> typing.Literal["o_bool_value"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_o_enum_value", b"_o_enum_value"]) -> typing.Literal["o_enum_value"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_o_float_value", b"_o_float_value"]) -> typing.Literal["o_float_value"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_o_int_value", b"_o_int_value"]) -> typing.Literal["o_int_value"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_o_name", b"_o_name"]) -> typing.Literal["o_name"] | None: ...

global___BasicMessageA = BasicMessageA
