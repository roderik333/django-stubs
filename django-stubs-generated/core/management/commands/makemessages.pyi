from typing import Any, List, Optional, Tuple

from django.core.management.base import BaseCommand, CommandParser

plural_forms_re: Any
STATUS_OK: int
NO_LOCALE_DIR: Any

def check_programs(*programs: Any) -> None: ...

class TranslatableFile:
    file: str = ...
    dirpath: str = ...
    locale_dir: str = ...
    def __init__(self, dirpath: str, file_name: str, locale_dir: Any) -> None: ...
    def __eq__(self, other: TranslatableFile) -> bool: ...
    def __lt__(self, other: TranslatableFile) -> bool: ...
    @property
    def path(self) -> str: ...

class BuildFile:
    command: django.core.management.commands.makemessages.Command = ...
    domain: str = ...
    translatable: django.core.management.commands.makemessages.TranslatableFile = ...
    def __init__(self, command: Command, domain: str, translatable: TranslatableFile) -> None: ...
    def is_templatized(self) -> bool: ...
    def path(self) -> str: ...
    def work_path(self) -> str: ...
    def preprocess(self) -> None: ...
    def postprocess_messages(self, msgs: str) -> str: ...
    def cleanup(self) -> None: ...

def normalize_eols(raw_contents: str) -> str: ...
def write_pot_file(potfile: str, msgs: str) -> None: ...

class Command(BaseCommand):
    stderr: django.core.management.base.OutputWrapper
    stdout: django.core.management.base.OutputWrapper
    style: django.core.management.color.Style
    help: str = ...
    translatable_file_class: Any = ...
    build_file_class: Any = ...
    requires_system_checks: bool = ...
    msgmerge_options: Any = ...
    msguniq_options: Any = ...
    msgattrib_options: Any = ...
    xgettext_options: Any = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    domain: Any = ...
    verbosity: Any = ...
    symlinks: Any = ...
    ignore_patterns: Any = ...
    no_obsolete: Any = ...
    keep_pot: Any = ...
    extensions: Any = ...
    invoked_for_django: bool = ...
    locale_paths: Any = ...
    default_locale_path: Any = ...
    def handle(self, *args: Any, **options: Any) -> None: ...
    def gettext_version(self) -> Tuple[int, int]: ...
    def settings_available(self) -> bool: ...
    def build_potfiles(self) -> List[str]: ...
    def remove_potfiles(self) -> None: ...
    def find_files(self, root: str) -> List[TranslatableFile]: ...
    def process_files(self, file_list: List[TranslatableFile]) -> None: ...
    def process_locale_dir(self, locale_dir: Any, files: List[TranslatableFile]) -> None: ...
    def write_po_file(self, potfile: str, locale: str) -> None: ...
    def copy_plural_forms(self, msgs: str, locale: str) -> str: ...
