from json import JSONDecoder


class Request:
    def __init__(self, body: bytes, scope: dict):
        self.body: bytes = body
        self.params: str = scope['query_string'].decode()
        self.client: tuple[str, int] = scope['client']
        self.headers: dict[str, str] = {k.decode(): v.decode() for k, v in scope['headers']}

    def __decode_body(self, encoding):
        return self.body.decode(encoding)
    
    def json(self, encoding='utf-8', check_headers=False) -> dict:
        if check_headers:
            assert (ct := self.headers.get('content-type'))
            assert ct == 'application/json'
        
        return JSONDecoder().decode(self.__decode_body(encoding))
    
    def text(self, encoding='utf-8', check_headers=False) -> str:
        if check_headers:
            assert (ct := self.headers.get('content-type'))
            assert ct == 'text/plain'

        return self.__decode_body(encoding)
