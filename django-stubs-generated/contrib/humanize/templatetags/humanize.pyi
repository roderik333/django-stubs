from datetime import date, datetime
from decimal import Decimal
from typing import Any, Optional, Union

register: Any

def ordinal(value: Optional[str]) -> Optional[str]: ...
def intcomma(value: Optional[Union[Decimal, float, str]], use_l10n: bool = ...) -> str: ...

intword_converters: Any

def intword(value: Optional[str]) -> Optional[Union[int, str]]: ...
def apnumber(value: Optional[str]) -> Optional[Union[int, str]]: ...
def naturalday(value: Optional[Union[date, str]], arg: None = ...) -> Optional[str]: ...
def naturaltime(value: datetime) -> str: ...
