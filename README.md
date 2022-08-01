# DHT Sensor Pi

This repository contains the required code to read DHT inputs from DHT sensors. It prints out the Temperature and Humidity. Optionally, sends the outputs to the
[Watson IoT Platform](https://internetofthings.ibmcloud.com/) (requires service credentials).

## How to use it?

Run the following to install all dependencies

`python3 -m pip install -r requirements.txt`

After installing the dependencies, run the following command to start the application.

`python3 server.py --pin <SENSOR_PIN_NUMBER>`

## How to send data to Watson IoT Platform

Create a `.env` file in the root folder of this repository with the following variables:

```
WATSON_IOT_ORG = YOUR_ORG
WATSON_IOT_DEVICE_TYPE = YOUR_DEVICE 
WATSON_IOT_TOKEN = YOUR_IOT_DEVICE_TOKEN
WATSON_IOT_DEVICE_ID = YOUR_IOT_DEVICE_ID
```

Run the following command:

`python3 server.py --pin <SENSOR_PIN_NUMBER> --watson`

The properties used on this application are:

Temperature
- Event: `dht11`
- Property: `temperature`

Humidity
- Event: `dht11`
- Property: `humidity`

Learn more about how to setup your device on Watson IoT Platform account using [this tutorial](https://iotdesignpro.com/projects/how-to-send-sensor-data-to-ibm-watson-cloud-platform-using-raspberry-pi).

## How to run it using an `.env` file

Optionally, you can run this application using a `.env` file instead of command arguments.

Create a `.env` file in the root folder of this repository with the following variables:


```
# application properties
DHT_SENSOR_PIN = SENSOR_PIN_NUMBER
ENABLE_WATSON_IOT_PLATFORM = TRUE_OR_FALSE

# watson iof platform properties
WATSON_IOT_ORG = YOUR_ORG
WATSON_IOT_DEVICE_TYPE = YOUR_DEVICE 
WATSON_IOT_TOKEN = YOUR_IOT_DEVICE_TOKEN
WATSON_IOT_DEVICE_ID = YOUR_IOT_DEVICE_ID
```

Run the followig command to start the application:

`python3 server.py`