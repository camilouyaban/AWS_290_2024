from collections.abc import Iterable
from re import Pattern
from typing import Literal, overload

# class is entirely undocumented
class FileList:
    allfiles: Iterable[str] | None
    files: list[str]
    def __init__(self, warn: None = ..., debug_print: None = ...) -> None: ...
    def set_allfiles(self, allfiles: Iterable[str]) -> None: ...
    def findall(self, dir: str = ...) -> None: ...
    def debug_print(self, msg: str) -> None: ...
    def append(self, item: str) -> None: ...
    def extend(self, items: Iterable[str]) -> None: ...
    def sort(self) -> None: ...
    def remove_duplicates(self) -> None: ...
    def process_template_line(self, line: str) -> None: ...
    @overload
    def include_pattern(
        self, pattern: str, anchor: bool = True, prefix: str | None = ..., is_regex: Literal[0, False] = 0
    ) -> bool: ...
    @overload
    def include_pattern(self, pattern: str | Pattern[str], *, is_regex: Literal[True, 1]) -> bool: ...
    @overload
    def include_pattern(
        self, pattern: str | Pattern[str], anchor: bool = True, prefix: str | None = ..., is_regex: bool = False
    ) -> bool: ...
    @overload
    def exclude_pattern(
        self, pattern: str, anchor: bool = True, prefix: str | None = ..., is_regex: Literal[0, False] = 0
    ) -> bool: ...
    @overload
    def exclude_pattern(self, pattern: str | Pattern[str], *, is_regex: Literal[True, 1]) -> bool: ...
    @overload
    def exclude_pattern(
        self, pattern: str | Pattern[str], anchor: bool = True, prefix: str | None = ..., is_regex: bool = False
    ) -> bool: ...