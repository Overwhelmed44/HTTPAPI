from .handler import Handler, HandlerFunc
from typing import Callable


class HTTPAPI:
    def __init__(self):
        self.__endpoints: dict[str, Handler] = {}
    
    @property
    def endpoints(self):
        return self.__endpoints

    def get(self, path: str) -> Callable[[HandlerFunc], HandlerFunc]:
        def bind(handler: HandlerFunc) -> HandlerFunc:
            self.__endpoints[path + "-GET"] = Handler(handler)
            return handler
        return bind
    
    def post(self, path: str) -> Callable[[HandlerFunc], HandlerFunc]:
        def bind(handler: HandlerFunc) -> HandlerFunc:
            self.__endpoints[path + "-POST"] = Handler(handler)
            return handler
        return bind

    def put(self, path: str) -> Callable[[HandlerFunc], HandlerFunc]:
        def bind(handler: HandlerFunc) -> HandlerFunc:
            self.__endpoints[path + "-PUT"] = Handler(handler)
            return handler
        return bind
    
    def delete(self, path: str) -> Callable[[HandlerFunc], HandlerFunc]:
        def bind(handler: HandlerFunc) -> HandlerFunc:
            self.__endpoints[path + "-DELETE"] = Handler(handler)
            return handler
        return bind
    
    async def __call__(self, scope, recv, send) -> None:
        assert scope['type'] == 'http'

        await self.__endpoints[scope['path'] + '-' + scope['method']](scope, recv, send)
