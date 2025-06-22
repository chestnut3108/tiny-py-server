import socket

def start_server(router, host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

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

        if router.does_path_exist(path):
            handler = router.get_handler(path)
        else:
            handler = router.get_handler('/')

        response = handler()
        client_conn.sendall(response.encode())
        client_conn.close()