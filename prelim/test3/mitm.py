from network import LoRa
import socket
import time

# Man-in-the-Middle LoPy essentially logs all received communication in hexadecimal
# It stays the same throughout the tests


def to_hex(data):
    """
        Args:
            - data: A bytes object
        Returns:
            The hexadecimal representation of the data
    """
    return ":".join("{:02x}".format(char) for char in data)


lora = LoRa(mode=LoRa.LORA, frequency=868100000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)

while True:
    msg = s.recv(255)
    print("Received {}".format(to_hex(msg)))
    time.sleep(0.01)
