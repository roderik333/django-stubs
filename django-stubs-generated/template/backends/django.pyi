from typing import Any, Dict, Iterator, Optional

from django.http.request import HttpRequest
from django.template.base import Origin, Template
from django.template.exceptions import TemplateDoesNotExist
from django.utils.safestring import SafeText

from .base import BaseEngine

class DjangoTemplates(BaseEngine):
    app_dirs: bool
    dirs: List[str]
    name: str
    app_dirname: str = ...
    engine: django.template.engine.Engine = ...
    def __init__(self, params: Dict[str, Any]) -> None: ...
    def from_string(self, template_code: str) -> Template: ...
    def get_template(self, template_name: str) -> Template: ...
    def get_templatetag_libraries(self, custom_libraries: Dict[str, str]) -> Dict[str, str]: ...

class Template:
    template: django.template.base.Template = ...
    backend: django.template.backends.django.DjangoTemplates = ...
    def __init__(self, template: Template, backend: DjangoTemplates) -> None: ...
    @property
    def origin(self) -> Origin: ...
    def render(self, context: Any = ..., request: Optional[HttpRequest] = ...) -> SafeText: ...

def copy_exception(exc: TemplateDoesNotExist, backend: Optional[DjangoTemplates] = ...) -> TemplateDoesNotExist: ...
def reraise(exc: TemplateDoesNotExist, backend: DjangoTemplates) -> Any: ...
def get_installed_libraries() -> Dict[str, str]: ...
def get_package_libraries(pkg: Any) -> Iterator[str]: ...
