import socket
from constants.HttpConstants import *
from utils.HttpRequest import HttpRequest
from urllib.parse import parse_qs

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
            request_line = request_data.splitlines()[0]
            method, path, _ = request_line.split()
        except Exception:
            path = '/'

        path, _, query_params = path.partition('?')
        query_params = parse_qs(query_params)
        print("path " + path)
        print("query_params {}" .format( query_params))


        handler = router.get_handler(path, method)
        
        httpRequest = HttpRequest(None, query_params, None)

        response = handler(httpRequest)
        client_conn.sendall(response.encode())
        client_conn.close()