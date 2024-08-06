from json import JSONEncoder


class Response:
    CONTENT_TYPE = None

    def __init__(self, body, status=200):
        self.body = self.serialize(body)
        self.status = status
        self.headers = [(b'content-type', self.__content_type())]
    
    @staticmethod
    def serialize(body):
        raise NotImplementedError
    
    @classmethod
    def __content_type(cls):
        return cls.CONTENT_TYPE


class StatusResponse(Response):
    def __init__(self, status=200):
        self.body = b''
        self.status = status
        self.headers = [(b'content-type', b'text/plain')]
    

class JSONResponse(Response):
    CONTENT_TYPE = b'application/json'

    @staticmethod
    def serialize(body):
        return JSONEncoder().encode(body).encode()


class PlainTextResponse(Response):
    CONTENT_TYPE = b'text/plain'

    @staticmethod
    def serialize(body):
        return body.encode()
