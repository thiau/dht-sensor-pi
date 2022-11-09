# This code is based on Adafruit Learning
# https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup

import time
import adafruit_dht
import argparse
import os
from helpers.watson_iot_platform import IBMWatsonIoTPlatform
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(
    prog="server.py",
    description='Reads DHT sensors and prints the output. Optionally sends the outputs to the Watson IoT Platform (requires service credentials in .env).',
    usage='python3 %(prog)s [options]')

parser.add_argument('--pin', help='The PIN Number your DHT is connected to')
parser.add_argument('--watson', action='store_true', help="Sends outputs of the sensor to the Watson IoT Platform (requires service credentials in .env)")
parser.set_defaults(watson=False)

args = parser.parse_args()

pin = int(args.pin) if args.pin else int(os.getenv("SENSOR_PIN"))
enable_watson = args.watson or os.getenv(
    'ENABLE_WATSON_IOT_PLATFORM', 'False') == 'True'

dht_device = adafruit_dht.DHT11(pin)
iot_platform = IBMWatsonIoTPlatform() if enable_watson else None

while True:
    try:
        # Print the values to the serial port
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dht_device.humidity

        # publish temp message
        if iot_platform:
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
            f"Temp: {temperature_f} F / {temperature_c} C    Humidity: {humidity}%")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht_device.exit()
        raise error

    time.sleep(2.0)
