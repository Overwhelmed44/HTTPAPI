from json import JSONDecoder


class Request:
    def __init__(self, body, scope):
        self.body = body
        self.params = scope['query_string'].decode()
        self.client = scope['client']
        self.headers = {k.decode(): v.decode() for k, v in scope['headers']}

    def __decode_body(self, encoding):
        return self.body.decode(encoding)
    
    def json(self, encoding='utf-8'):
        assert (ct := self.headers.get('content-type'))
        assert ct == 'application/json'
        
        return JSONDecoder().decode(self.__decode_body(encoding))
    
    def text(self, encoding='utf-8'):
        assert (ct := self.headers.get('content-type'))
        assert ct == 'text/plain'

        return self.__decode_body(encoding)
