from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=868100000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)

while True:
    msg = s.recv(64)
    print("Received {}".format(msg))
    s.send('Pong')
    time.sleep(0.1)
