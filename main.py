import machine
import dht
import time

r = machine.Pin(2, machine.Pin.OUT)
d = dht.DHT11(machine.Pin(4))

while True:
    d.measure()
    c_temperature = d.temperature()
    c_humidity = d.humidity()
    if (c_temperature > 31) or (c_humidity > 70):
        r.value(1)
    else:
        r.value(0)
    print("Temperature = {} | Humidity = {}".format(c_temperature, c_humidity))
    time.sleep(5)