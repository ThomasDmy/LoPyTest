# Fuzzer client. This program sends garbage instead of proper Join Reqquest. The behavior of the receiving gateway is
# observed.

from network import LoRa
import ucrypto
import socket
import binascii
import time


def gen_datagram():
    """Generate random data, with a length between 0 and 255 bytes.

    Returns:
        a bytes object
    """
    length = ucrypto.getrandbits(32)[0]
    data = ucrypto.getrandbits(length * 8)[:length]
    return data

def to_hex(data):
    """
        Args:
            - data: A bytes object
        Returns:
            The hexadecimal representation of the data
    """
    return ":".join("{:02x}".format(char) for char in data)

# Configure the transceiver
lora = LoRa(mode=LoRa.LORA, frequency=868100000)

# Creates a socket for communication
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

s.setblocking(True)
while True:
    msg = gen_datagram()
    s.send(msg)
    # Check on the other side that messages match
    print("Sent: {}".format(to_hex(msg)))
    time.sleep(0.01)
