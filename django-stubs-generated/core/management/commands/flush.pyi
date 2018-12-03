from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    stderr: django.core.management.base.OutputWrapper
    stdout: django.core.management.base.OutputWrapper
    help: str = ...
    stealth_options: Any = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    style: django.core.management.color.Style = ...
    def handle(self, **options: Any) -> None: ...
