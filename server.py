import socket
import json

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 1024

server = socket.socket()
server.bind((IP, PORT))
server.listen()
print(f"[LISTENING] El servidor esta esperando conexiones en {IP}")

conn, addr = server.accept()
print(f"[CONNECTED] Nueva conexion en {addr}")

while True:
  
  heder= conn.recv(HEADER).decode("utf-8")
  header=json.loads(header)
  msg_len=header["length"]
  msg = conn.recv(msg_len).decode("utf-8")
  print (f"{header['from']} a las {header['timestamp']} dice:{msg}")
