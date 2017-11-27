from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=868100000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)

while True:
    print('Send Ping')
    s.send('Ping')
    time.sleep(0.1)
