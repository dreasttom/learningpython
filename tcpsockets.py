import socket
import threading
"""This is meant for students to learn basic TCP connection programming in pything. There are many other
similar code samples on the internet. It runs, but could certainly be improved. Students are expected to take this
and make it more robust. For example the exception handling is rather primitive """
def handle_clientconnection(client_socket):
  while True:
    try:
      data = client_socket.recv(1024).decode('utf-8')
      if not data:
        break
      print(f"Received from client: {data}")
      client_socket.sendall(f"Server received: {data}".encode('utf-8'))
    except:
      break
  client_socket.close()


def start_server(host, port):
  try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    while True:
      client_socket, client_address = server_socket.accept()
      print(f"Connection was accepted from {client_address}")
      client_handler = threading.Thread(target=handle_clientconnection, args=(client_socket,))
      client_handler.start()

  except:
    print("Error encountered in start_server")
def start_client(host, port, message):
  """Starts a TCP client."""
try:
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((host, port))
  client_socket.sendall(message.encode('utf-8'))
  data = client_socket.recv(1024).decode('utf-8')
  print(f"Received from server: {data}")
  client_socket.close()
  
except:
    print("Error encountered in start_client")
