from constants.HttpConstants import HTTP_REASON_PHRASES, HTTP_200_OK

class HttpResponse:
    def __init__(self):
        pass
    def prepareResponse(self, responseCode, contentType, content):
        reason = HTTP_REASON_PHRASES.get(responseCode, HTTP_200_OK)
        return (
        f"HTTP/1.1 {responseCode} {reason}\r\n"
        f"Content-Type: {contentType}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
        f"{content}"
    )