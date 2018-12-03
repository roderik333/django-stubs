from typing import Any, Dict, List, Optional, Tuple, Type, Union

from django.db.backends.ddl_references import Statement
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.models.base import Model

class Index:
    model: Type[django.db.models.base.Model]
    suffix: str = ...
    max_name_length: int = ...
    fields: List[str] = ...
    fields_orders: List[Tuple[str, str]] = ...
    name: str = ...
    db_tablespace: Optional[str] = ...
    def __init__(self, *, fields: Any = ..., name: Optional[Any] = ..., db_tablespace: Optional[Any] = ...) -> None: ...
    def check_name(self) -> List[str]: ...
    def create_sql(self, model: Type[Model], schema_editor: DatabaseSchemaEditor, using: str = ...) -> Statement: ...
    def remove_sql(self, model: Type[Model], schema_editor: DatabaseSchemaEditor) -> str: ...
    def deconstruct(self) -> Tuple[str, Tuple, Dict[str, Union[List[str], str]]]: ...
    def clone(self) -> Index: ...
    def set_name_with_model(self, model: Type[Model]) -> None: ...
    def __eq__(self, other: Index) -> bool: ...
