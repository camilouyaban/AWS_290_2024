from _typeshed.wsgi import WSGIEnvironment
from collections.abc import Iterator, MutableMapping

from webob.multidict import MultiDict

class ResponseHeaders(MultiDict[str, str]): ...

class EnvironHeaders(MutableMapping[str, str]):
    environ: WSGIEnvironment
    def __init__(self, environ: WSGIEnvironment) -> None: ...
    def __getitem__(self, hname: str) -> str: ...
    def __setitem__(self, hname: str, value: str) -> None: ...
    def __delitem__(self, hname: str) -> None: ...
    def keys(self) -> list[str]: ...  # type: ignore[override]
    def __contains__(self, hname: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
