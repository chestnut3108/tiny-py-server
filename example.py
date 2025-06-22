# main.py

from Router import Router
from utils.HttpResponse import HttpResponse
from constants.HttpConstants import *
from server import start_server

router = Router()

@router.route('/test1', HTTP_METHOD_GET)
def test1():
    return HttpResponse().prepareResponse(
        HTTP_200_OK,
        CONTENT_TYPE_TEXT_HTML,
        "<html><body><h1>test 11!</h1></body></html>"
    )

@router.route('/test2', HTTP_METHOD_GET)
def test2():
    return HttpResponse().prepareResponse(
        HTTP_200_OK,
        CONTENT_TYPE_TEXT_HTML,
        "<html><body><h1>test 22!</h1></body></html>"
    )

@router.route('/', HTTP_METHOD_GET)
def default_handler():
    return HttpResponse().prepareResponse(
        HTTP_404_NOT_FOUND,
        CONTENT_TYPE_TEXT_HTML,
        "<html><body><h1>Please implement this method!</h1></body></html>"
    )

# Start the server
start_server(router)
