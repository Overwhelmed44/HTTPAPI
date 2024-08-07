from json import JSONEncoder
from typing import Any


class Response:
    CONTENT_TYPE = b''

    def __init__(self, body: Any, status: int = 200, headers: dict[str, str] | None = None):
        self.body = self.serialize(body)
        self.status = status
        self.headers = list({k.encode(): headers[k].encode() for k in headers}.items()) if headers else []

        if ct := self.__content_type():
            self.headers.append((b'content-type', ct))
    
    @staticmethod
    def serialize(body: bytes) -> bytes:
        return body
    
    @classmethod
    def __content_type(cls) -> bytes:
        return cls.CONTENT_TYPE
    

class JSONResponse(Response):
    CONTENT_TYPE = b'application/json'

    @staticmethod
    def serialize(body: Any) -> bytes:
        return JSONEncoder().encode(body).encode()


class PlainTextResponse(Response):
    CONTENT_TYPE = b'text/plain'

    @staticmethod
    def serialize(body: Any) -> bytes:
        return body.encode()


class StatusResponse(Response):
    CONTENT_TYPE = b'text/plain'

    def __init__(self, status: int = 200):
        super().__init__(b'', status)
