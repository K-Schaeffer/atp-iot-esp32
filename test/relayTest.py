#           Author: Kauan Schaeffer             #
# Description: Program to test relay connection #

import machine
import time

r = machine.Pin(2, machine.Pin.OUT)

while True:
    r.value(1)
    time.sleep(2)
    r.value(0)
    time.sleep(2)
