#           Author: Kauan Schaeffer             #
# Description: Measure temperature and humidity #
# with DHT11 sensor and controll relay          #

def connect_devices():
    import machine # Lib used to controll devices
    relay = machine.Pin(2, machine.Pin.OUT)
    
    import dht # Lib used to controll the DHT11
    dht11 = dht.DHT11(machine.Pin(4))
    
    return relay, dht11

def measure():
    relay, dht11 = connect_devices()
    
    dht11.measure() #Measure the enviroment
    current_temperature = dht11.temperature()
    current_humidity = dht11.humidity()
    
    if (current_temperature > 31) or (current_humidity > 70):
        relay.value(1) # Turn relay on if temperature greater than 31 or humidity greater than 70%
    else:
        relay.value(0)
        
    return current_temperature, current_humidity
