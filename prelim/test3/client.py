from network import LoRa
import socket
import binascii
import struct
import time

# We speak LoRaWAN.
lora = LoRa(mode=LoRa.LORAWAN)

# Device ID, must match with the one provided to AS
dev_eui = binascii.unhexlify('AA BB CC DD EE FF 77 78'.replace(' ', ''))
# Application ID, must match with the AS
app_eui = binascii.unhexlify('70 B3 D5 7E D0 00 7C 00'.replace(' ', ''))
# Application key as created by the AS
app_key = binascii.unhexlify('EB 1F C2 C9 99 A2 10 F3 FA 49 0A 16 B7 91 55 9F'.replace(' ', ''))

# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
lora.add_channel(0, frequency=868100000, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=868100000, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=868100000, dr_min=0, dr_max=5)

# Authentication to the WAN
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# Connection takes ~10sec
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

# Remove other channels
for i in range(3, 16):
    lora.remove_channel(i)

# Creates a socket for communication
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# Set datarate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socketnon-blocking
s.setblocking(False)

print("Connected, start sending messages")

# Now send messages, check monitoring interface if they are received on the application side
i = 1
while True:
    s.send(b'PKT #' + bytes([i]))
    time.sleep(5)
    i += 1
