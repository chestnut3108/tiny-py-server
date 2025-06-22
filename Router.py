from constants.HttpConstants import HTTP_404_NOT_FOUND


class Router:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        print('route {}, path {}', self.routes, path)
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    
    def does_path_exist(self, path):
        if (self.routes.get(path) != None):
            return True
        else: 
            return False

    def get_handler(self, path):
        return self.routes.get(path, self.not_found)

    def not_found(self):
        raise Exception("Method not found")