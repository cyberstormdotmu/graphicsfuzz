# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Binary(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    path = ... # type: typing___Text
    version = ... # type: typing___Text

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        path : typing___Optional[typing___Text] = None,
        version : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Binary: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"name",u"path",u"tags",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"path",b"path",u"tags",b"tags",u"version",b"version"]) -> None: ...

class Archive(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    url = ... # type: typing___Text
    output_file = ... # type: typing___Text
    output_directory = ... # type: typing___Text

    def __init__(self,
        *,
        url : typing___Optional[typing___Text] = None,
        output_file : typing___Optional[typing___Text] = None,
        output_directory : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Archive: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"output_directory",u"output_file",u"url"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"output_directory",b"output_directory",u"output_file",b"output_file",u"url",b"url"]) -> None: ...

class ArchiveSet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def archives(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Archive]: ...

    @property
    def binaries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Binary]: ...

    def __init__(self,
        *,
        archives : typing___Optional[typing___Iterable[Archive]] = None,
        binaries : typing___Optional[typing___Iterable[Binary]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ArchiveSet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"archives",u"binaries"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"archives",b"archives",u"binaries",b"binaries"]) -> None: ...