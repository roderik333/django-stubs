from typing import Any, Callable, Dict, List, Optional, Type, Union
from unittest.mock import Mock

from django.apps.config import AppConfig
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model

DEFAULT_DB_ALIAS: str
DJANGO_VERSION_PICKLE_KEY: str

class Error(Exception): ...
class InterfaceError(Error): ...
class DatabaseError(Error): ...
class DataError(DatabaseError): ...
class OperationalError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InternalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...

class DatabaseErrorWrapper:
    wrapper: django.db.backends.sqlite3.base.DatabaseWrapper = ...
    def __init__(self, wrapper: DatabaseWrapper) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: None, exc_value: None, traceback: None) -> None: ...
    def __call__(self, func: Callable) -> Callable: ...

def load_backend(backend_name: str) -> Any: ...

class ConnectionDoesNotExist(Exception): ...

class ConnectionHandler:
    databases: Dict[str, Dict[str, Optional[Union[Dict[str, Optional[bool]], int, str]]]]
    def __init__(self, databases: Dict[str, Dict[str, Union[Dict[str, str], str]]] = ...) -> None: ...
    def databases(self) -> Dict[str, Union[Dict[str, Union[Dict[str, bool], str]], Dict[str, Union[Dict[str, str], str]]]]: ...
    def ensure_defaults(self, alias: str) -> None: ...
    def prepare_test_settings(self, alias: str) -> None: ...
    def __getitem__(self, alias: str) -> BaseDatabaseWrapper: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self): ...
    def all(self) -> List[DatabaseWrapper]: ...
    def close_all(self) -> None: ...

class ConnectionRouter:
    routers: List[Any]
    def __init__(self, routers: None = ...) -> None: ...
    def routers(self) -> List[Mock]: ...
    db_for_read: Any = ...
    db_for_write: Any = ...
    def allow_relation(self, obj1: Model, obj2: Model, **hints: Any) -> bool: ...
    def allow_migrate(self, db: str, app_label: str, **hints: Any) -> bool: ...
    def allow_migrate_model(self, db: str, model: Type[Model]) -> bool: ...
    def get_migratable_models(self, app_config: AppConfig, db: str, include_auto_created: bool = ...) -> List[Type[Model]]: ...
