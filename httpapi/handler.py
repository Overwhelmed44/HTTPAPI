from typing import Callable, Coroutine
from .responses import Response
from .request import Request

type HandlerFunc = Callable[[Request], Coroutine[None, None, Response]]


class Handler:
    def __init__(self, handler: HandlerFunc):
        self.handler = handler

    @staticmethod
    async def __get_full_body(recv) -> bytes:
        rv = await recv()
        data = rv['body']

        while rv['more_body']:
            rv = await recv()
            data += rv['body']
        
        return data

    async def __call__(self, scope, recv, send) -> None:
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
