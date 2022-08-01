import os
import json
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

class IBMWatsonIoTPlatform:
    def __init__(self):
        self.org = os.getenv('WATSON_IOT_ORG')
        self.device_type = os.getenv('WATSON_IOT_DEVICE_TYPE')
        self.device_id = os.getenv('WATSON_IOT_DEVICE_ID')
        self.token = os.getenv('WATSON_IOT_TOKEN')
        
        # Set mqtt variables
        self.server = f"{self.org}.messaging.internetofthings.ibmcloud.com"
        self.auth_method = "use-token-auth"
        self.client_id = f"d:{self.org}:{self.device_type}:{self.device_id}"
        self.mqttc = None

    def connect(self):
        self.mqttc = mqtt.Client(client_id=self.client_id)
        self.mqttc.username_pw_set(self.auth_method, self.token)
        self.mqttc.connect(self.server, 1883, 60)

    def publish(self, event, property, value):
        payload = dict()
        payload[property] = value

        # set topic based on iot plat. event
        topic = f"iot-2/evt/{event}/fmt/json"
        
        self.connect()
        self.mqttc.publish(topic, json.dumps(payload))

