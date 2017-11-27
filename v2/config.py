""" LoPy LoRaWAN Nano Gateway configuration options """

# specified in when registering your gateway
GATEWAY_ID = '1188227733664455'

# server address & port to forward received data to
SERVER = 'router.eu.thethings.network'
PORT = 1700

# NTP server for getting/setting time
NTP = "pool.ntp.org"

# NTP server polling interval
NTP_PERIOD_S = 3600

# Wi-Fi settings
WIFI_SSID = 'FD-51'
WIFI_PASS = 'fromage2chevre'

# check your specifc region for LORA_FREQUENCY and LORA_DR (datarate)
LORA_FREQUENCY = 868100000

# datarate 5
LORA_DR = "SF7BW125"
