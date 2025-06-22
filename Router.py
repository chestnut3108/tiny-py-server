from constants.HttpConstants import HTTP_404_NOT_FOUND


class Router:
    def __init__(self):
        self.routes = {}
        not_found_handler_method = None

    def route(self, path, method):
        def decorator(func):
            self.routes[(path, method.upper())] = func
            return func
        return decorator

    def print_routes(self):
        for url, method in self.routes:
            print("registering API endpoint with url {} method {}".format(url, method))

    def does_path_exist(self, path, method):
        return (path, method.upper()) in self.routes

    def get_handler(self, path, method):
        return self.routes.get((path, method.upper()), self.not_found_handler_method)

    def not_found_handler_method(self, not_found_handler_method):
        self.not_found_handler_method = not_found_handler_method 