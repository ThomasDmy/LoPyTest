# Legitimate client, it only sends Join Request

from network import LoRa
import binascii
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

while True:
    # Authentication to the WAN
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)
    # The connection is a bottleneck, we do not have the hand on the Connection
    # delay, the subsequent calls to join do not actually send trigger an emission
    # To improve that, one could modify the implementation of the LoRa stack
    # on the ESP32. 
    time.sleep(0.5)
