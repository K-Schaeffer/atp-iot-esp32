#           Author: Kauan Schaeffer             #
# Description: Connect ESP32 microprocessor     #
# into a WIFI network and send data to server   #

def connect(ssid, password):
    import network #Lib used to connect into networks
    import time
    
    print("Connecting...")

    station = network.WLAN(network.STA_IF) #Connecting and activating the ESP32 into WLAN network
    station.active(True)
    station.connect(ssid, password)
    
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station
    
def send_data(c_temperature, c_humidity):
    import urequests
    
    print('========= Thingspeak Data ==========')
    print("Opening API endpoint...")
    
    #Request to server API
    response = urequests.get("http://api.thingspeak.com/update?api_key=SNUDWZOU5C89BLZQ&field1={}&field2={}".format(c_temperature, c_humidity))
    if response.text:
        print("Data sent successfully!")
        print('====================================\n')
    else:
        print("Couldn't connect to Thingspeak")
        print('====================================\n')

# More interesting methods from network lib

#station.disconnect() --> Disconnect
#station.scan() --> Scan for WIFI Networks
#station.ifconfig() --> Check IP's: esp32 ip / ipmask / default gateway / dns ip