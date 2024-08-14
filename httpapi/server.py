from .handler import Handler, HandlerFunc
from typing import Callable


class HTTPAPI:
    def __init__(self):
        self.__handlers: dict[str, Handler] = {}

    def get(self, path: str) -> Callable[[HandlerFunc | Handler], Handler]:
        def bind(handler: HandlerFunc | Handler) -> Handler:
            if not isinstance(handler, Handler):
                handler = Handler(handler)
            self.__handlers[path + "-GET"] = handler
            return handler
        return bind
    
    def post(self, path: str) -> Callable[[HandlerFunc | Handler], Handler]:
        def bind(handler: HandlerFunc | Handler) -> Handler:
            if not isinstance(handler, Handler):
                handler = Handler(handler)
            self.__handlers[path + "-POST"] = handler
            return handler
        return bind

    def put(self, path: str) -> Callable[[HandlerFunc | Handler], Handler]:
        def bind(handler: HandlerFunc | Handler) -> Handler:
            if not isinstance(handler, Handler):
                handler = Handler(handler)
            self.__handlers[path + "-PUT"] = handler
            return handler
        return bind
    
    def delete(self, path: str) -> Callable[[HandlerFunc | Handler], Handler]:
        def bind(handler: HandlerFunc | Handler) -> Handler:
            if not isinstance(handler, Handler):
                handler = Handler(handler)
            self.__handlers[path + "-DELETE"] = handler
            return handler
        return bind
    
    async def __call__(self, scope, recv, send) -> None:
        assert scope['type'] == 'http'

        await self.__handlers[scope['path'] + '-' + scope['method']](scope, recv, send)
