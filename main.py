#           Author: Kauan Schaeffer             #
# Description: Program to measure the temper... #
# ...ature and humidty, sending data to Thing.. #
# ..speak and turning the relay on/off          #

from wifi_lib import connect
import urequests

print("Connecting...")
station = connect("Oi_DB09", "zncp32Fa")
if not station.isconnected():
    print("Connection failed!")
else:
    print("Successfully connected!")
    print("Opening API endpoint...")
    response = urequests.get("http://api.thingspeak.com/update?api_key=HYFN2WWEGLEXE3IM&field1=3")
    if response.text:
        print("Success!")
        print("Page response: " + response.text)
    station.disconnect()

        






