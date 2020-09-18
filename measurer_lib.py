#           Author: Kauan Schaeffer             #
# Description: Measure temperature and humidity #
# with DHT11 sensor                             #

def connect_devices():
    import machine # Lib used to controll devices
    relay = machine.Pin(2, machine.Pin.OUT)
    
    import dht # Lib used to controll the DHT11
    dht11 = dht.DHT11(machine.Pin(4))
    
    return relay, dht11

def measure():
    import time # Lib used to break the code timing
    relay, dht11 = connect_devices()
    while True:
        dht11.measure()
        current_temperature = dht11.temperature()
        current_humidity = dht11.humidity()
        if (current_temperature > 31) or (current_humidity > 70):
            relay.value(1) # Turn relay on if temperature greater than 31 or 70%
        else:
            relay.value(0)
        print("Temperature = {} | Humidity = {}".format(current_temperature, current_humidity))
        time.sleep(5)            
