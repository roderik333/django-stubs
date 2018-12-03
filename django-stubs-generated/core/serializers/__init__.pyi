from collections import OrderedDict
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, Type, Union

from django.apps.config import AppConfig
from django.core.serializers.base import Serializer
from django.core.serializers.xml_serializer import Deserializer
from django.db.models.base import Model
from django.db.models.query import QuerySet

BUILTIN_SERIALIZERS: Any

class BadSerializer:
    internal_use_only: bool = ...
    exception: ModuleNotFoundError = ...
    def __init__(self, exception: ImportError) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

def register_serializer(format: str, serializer_module: str, serializers: Optional[Dict[str, Any]] = ...) -> None: ...
def unregister_serializer(format: str) -> None: ...
def get_serializer(format: str) -> Union[Type[Serializer], BadSerializer]: ...
def get_serializer_formats() -> List[str]: ...
def get_public_serializer_formats() -> List[str]: ...
def get_deserializer(format: str) -> Union[Callable, Type[Deserializer]]: ...
def serialize(
    format: str, queryset: Union[Iterator[Any], List[Model], QuerySet], **options: Any
) -> Optional[Union[List[OrderedDict], bytes, str]]: ...
def deserialize(format: str, stream_or_string: Any, **options: Any) -> Union[Iterator[Any], Deserializer]: ...
def sort_dependencies(
    app_list: Union[List[Tuple[AppConfig, None]], List[Tuple[str, List[Type[Model]]]]]
) -> List[Type[Model]]: ...
