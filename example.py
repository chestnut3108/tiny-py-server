# main.py

from Router import Router
from utils.HttpResponse import HttpResponse
from constants.HttpConstants import *
from server import start_server
from utils.HttpRequest import HttpRequest
router = Router()

@router.route('/test1', HTTP_METHOD_GET)
def test1( httpRequest):
    return HttpResponse().prepareResponse(
        HTTP_200_OK,
        CONTENT_TYPE_TEXT_HTML,
        "<html><body><h1>test 11!</h1></body></html>"
    )

@router.route('/test2', HTTP_METHOD_GET)
def test2( httpRequest):
    print(httpRequest.query_params)
    return HttpResponse().prepareResponse(
        HTTP_200_OK,
        CONTENT_TYPE_TEXT_HTML,
        "<html><body><h1>test 22!</h1></body></html>"
    )

def default_handler( httpRequest):
    return HttpResponse().prepareResponse(
        HTTP_404_NOT_FOUND,
        CONTENT_TYPE_TEXT_HTML,
        "<html><body><h1>Please implement this method!</h1></body></html>"
    )

router.not_found_handler_method(default_handler)
# Start the server
start_server(router)
