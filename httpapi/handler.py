from .request import Request


class Handler:
    def __init__(self, handler):
        self.handler = handler
    
    @staticmethod
    async def __get_full_body(recv) -> bytes:
        rv = await recv()
        data = rv['body']

        while rv['more_body']:
            rv = await recv()
            data += rv['body']
        
        return data

    def __call__(self, scope):
        async def _handle(recv, send):
            await self.handle(scope, recv, send)
        return _handle

    async def handle(self, scope, recv, send):
        body = await self.__get_full_body(recv)

        response = await self.handler(Request(body, scope))
                                 
        await send({
            "type": "http.response.start",
            "status": response.status,
            "headers": response.headers
        })

        await send({
            "type": "http.response.body",
            "body": response.body,
        })
