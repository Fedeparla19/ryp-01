import socket
import datetime
import json 

IP = "192.168.1.191" #socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 1024
header={
  "to":IP,
  "from":IP,
  "length":0,
  "timestamp":0
}

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
  
  msg = input("Ingrese un mensaje: ")
  header["length"]=len(msg)
  header["timestamp"]=str(datetime.datetime.now())
  obj=json.dumps(header)
  client.send(str(obj).encode("utf-8"))
  client.send(msg.encode("utf-8"))
