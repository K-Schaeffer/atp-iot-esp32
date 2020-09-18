#           Author: Kauan Schaeffer             #
# Description: Program to collect the temper... #
# ...ature and humidty, sending data to Thing.. #
# ..speak server                                #

# Imports area
from measurer_lib import measure
from wifi_lib import connect, send_data
import time

result = connect("Oi_DB09", "zncp32Fa") #Connect to WIFI

if not result.isconnected(): #If connection fail abort program
    print('Connection failed!')
    print('Aborting execution...')
elif result.isconnected():
    print('Connected successfully!\n')
    while True: # While true, keep measuring
        c_temperature, c_humidity = measure()
        
        print('========= Temperature Data =========')
        print("  Temperature = {} | Humidity = {}".format(c_temperature, c_humidity))
        print('====================================\n')
        
        send_data(c_temperature, c_humidity) #Send data to server
        time.sleep(5)
        print('\n\n')
        
    







