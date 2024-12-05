import socket


data = {}

def handle_request(request):
    
    parts = request.strip().split(' ', 2)
    command = parts[0].lower()

    if command == "get":
        if len(parts) != 2:
            return "Error: invalid get command"
        key = parts[1].strip('"')
        value = data.get(key)
        if value is not None:
            return f"Result: {value}"
        else:
            return "Error: empty value"

    elif command == "set":
        if len(parts) != 3:
            return "Error: invalid set command"
        key = parts[1].strip('"')
        value = parts[2]
        if value.isdigit():  
            data[key] = int(value)
            return "Result: value set successfully"
        else:
            return "Error: not a number"

    elif command == "getkeys":
        keys = ', '.join(data.keys())
        return f"Result: {keys}" if keys else "Error: no keys in data"

    else:
        return "Error: unknown command"

def start_server(host="127.0.0.1", port=53554):
   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"RPC сервер запущено на {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Підключено: {client_address}")
                request = client_socket.recv(1024).decode('utf-8')
                if not request:
                    continue
                print(f"Отримано запит: {request}")
                response = handle_request(request)
                client_socket.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()
