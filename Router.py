from constants.HttpConstants import HTTP_404_NOT_FOUND


class Router:
    def __init__(self):
        self.routes = {}

    def route(self, path, method):
        print('route {}, path {}', self.routes, path)
        def decorator(func):
            self.routes[(path, method.upper())] = func
            return func
        return decorator
    
    def does_path_exist(self, path, method):
        return (path, method.upper()) in self.routes

    def get_handler(self, path, method):
        return self.routes.get((path, method.upper()))

    def not_found(self):
        raise Exception("Method not found")