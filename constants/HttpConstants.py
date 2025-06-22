# --- Status Codes ---
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204
HTTP_301_MOVED_PERMANENTLY = 301
HTTP_302_FOUND = 302
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_502_BAD_GATEWAY = 502
HTTP_503_SERVICE_UNAVAILABLE = 503

# --- Reason Phrases ---
HTTP_REASON_PHRASES = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable"
}

# --- Content Types ---
CONTENT_TYPE_TEXT_HTML = 'text/html'
CONTENT_TYPE_TEXT_PLAIN = 'text/plain'
CONTENT_TYPE_APPLICATION_JSON = 'application/json'
CONTENT_TYPE_APPLICATION_XML = 'application/xml'
CONTENT_TYPE_TEXT_CSS = 'text/css'
CONTENT_TYPE_TEXT_JAVASCRIPT = 'text/javascript'
CONTENT_TYPE_IMAGE_PNG = 'image/png'
CONTENT_TYPE_IMAGE_JPEG = 'image/jpeg'
CONTENT_TYPE_IMAGE_GIF = 'image/gif'
CONTENT_TYPE_APPLICATION_OCTET_STREAM = 'application/octet-stream'

# --- Default Headers ---
DEFAULT_SERVER_NAME = 'PythonCustomHTTP/0.1'


HTTP_METHOD_POST = 'POST'
HTTP_METHOD_GET = 'GET'
HTTP_METHOD_PUT = 'PUT'