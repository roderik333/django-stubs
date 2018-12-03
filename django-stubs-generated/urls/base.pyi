from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
from uuid import UUID

from django.urls.resolvers import ResolverMatch

from .exceptions import NoReverseMatch, Resolver404
from .resolvers import get_ns_resolver, get_resolver
from .utils import get_callable

def resolve(path: str, urlconf: Optional[str] = ...) -> ResolverMatch: ...
def reverse(
    viewname: Optional[Union[Callable, str]],
    urlconf: Optional[str] = ...,
    args: Optional[Union[List[UUID], Tuple]] = ...,
    kwargs: Optional[Union[Dict[str, None], Dict[str, bytes], Dict[str, str], Dict[str, UUID]]] = ...,
    current_app: Optional[str] = ...,
) -> str: ...

reverse_lazy: Any

def clear_url_caches() -> None: ...
def set_script_prefix(prefix: str) -> None: ...
def get_script_prefix() -> str: ...
def clear_script_prefix() -> None: ...
def set_urlconf(urlconf_name: Optional[Union[Type[Any], str]]) -> None: ...
def get_urlconf(default: None = ...) -> Optional[Union[Type[Any], str]]: ...
def is_valid_path(path: str, urlconf: Optional[str] = ...) -> bool: ...
def translate_url(url: str, lang_code: str) -> str: ...
