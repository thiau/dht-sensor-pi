# This code is based on Adafruit Learning
# https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup

import time
import board
import adafruit_dht
from helpers.watson_iot_platform import IBMWatsonIoTPlatform

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D26)

# Create object for Watson IoT Platform tasks
iot_platform = IBMWatsonIoTPlatform()

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        
        # publish temp message
        iot_platform.publish(
            event="dht11", 
            property="temperature", 
            value=temperature_c)

        # publish humidity message
        iot_platform.publish(
            event="dht11", 
            property="humidity", 
            value=humidity)

        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)