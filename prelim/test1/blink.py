import pycom
import time

pycom.heartbeat(False)
while True:
    pycom.rgbled(0x550055)
    time.sleep(1)
    pycom.rgbled(0x000000)
    time.sleep(1)
