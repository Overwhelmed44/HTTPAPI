from .handler import Handler


class HTTPApi:
    def __init__(self):
        self.__endpoints = {}
    
    def __bound_handler(self, path, handler):
        self.__endpoints[path] = Handler(handler)
        
        return handler

    def get(self, path):
        return lambda handler: self.__bound_handler(path + 'GET', handler)
    
    def post(self, path):
        return lambda handler: self.__bound_handler(path + 'POST', handler)

    def put(self, path):
        return lambda handler: self.__bound_handler(path + 'PUT', handler)
    
    def delete(self, path):
        return lambda handler: self.__bound_handler(path + 'DELETE', handler)
    
    def __call__(self, scope):
        assert scope['type'] == 'http'

        return self.__endpoints[scope['path'] + scope['method']](scope)
