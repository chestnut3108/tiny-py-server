class HttpRequest:
    def __init__(self, headers, queryParams, requestBody):
        self.headers = headers
        self.queryParams = queryParams
        self.requestBody = requestBody
