import socket
from constants.HttpConstants import *
from utils.HttpRequest import HttpRequest
from utils.HttpRequest import HttpRequest

def start_server(router, host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    router.print_routes()

    print(f"Serving HTTP on {host}:{port}...")

    while True:
        client_conn, client_addr = server_socket.accept()
        request_data = client_conn.recv(1024).decode()

        print("Received request:")
        print(request_data)
        try:
            request = HttpRequest(request_data)
        except Exception:
            path = '/'

        print("path " + request.path)
        print("query_params {}" .format( request.query_params))


        handler = router.get_handler(request.path, request.method)
        
        response = handler(request)
        client_conn.sendall(response.encode())
        client_conn.close()