from urllib.parse import parse_qs

class HttpRequest:
    def __init__(self, request: str):
        self.request = request
        self.parseRequest(request)
    def __str__(self):
        return (
            f"Method: {self.method}\n"
            f"Path: {self.path}\n"
            f"Version: {self.version}\n"
            f"Headers: {self.headers}\n"
            f"query_params: {self.query_params}\n"
            f"Body: {self.body}"
        )
    
    def parseRequest(self, request: str):
        lines = request.split("\r\n")

        # Parse request line: METHOD PATH VERSION
        request_line = lines[0]
        self.method, self.path, self.version = request_line.split(" ")
        self.path, _, query_params = self.path.partition('?')
        self.query_params = parse_qs(query_params)

        # Parse headers
        headers = {}
        i = 1
        while i < len(lines) and lines[i] != "":
            key, value = lines[i].split(":", 1)
            headers[key.strip()] = value.strip()
            i += 1
        self.headers = headers

        # Parse body
        i += 1  # Skip blank line
        self.body = "\r\n".join(lines[i:]) if i < len(lines) else ""
