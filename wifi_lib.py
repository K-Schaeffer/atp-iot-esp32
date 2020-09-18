#           Author: Kauan Schaeffer             #
# Description: Connect ESP32 microprocessor     #
# into a WIFI network                           #

def connect(ssid, password):
    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station


#station.scan() --> Scan for WIFI Networks
#station.ifconfig() --> Check IP's: esp32 ip / ipmask / default gateway / dns ip