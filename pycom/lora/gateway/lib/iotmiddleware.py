from mqtt import MQTTClient
import time
import json


def sub_cb(self,topic, msg):
    print(msg)

class IotException(Exception):
    pass

class IotConnection:

    def __init__(self,client_id,server):
        self.client_id = client_id
        self.client = MQTTClient(client_id,server,port=1883)
        self.client.set_callback(sub_cb)
        self.client.connect()

    def send_temperature(self,topic,value):
        data = {
                    "temperature":{
                    "value":str(value),
                    "type":"number"
                    }
                }
        json_data = json.dumps(data)
        print(topic,json_data)
        self.client.publish(topic=topic, msg=json_data)

    def send_humidity(self,topic,value):
        data = {
                    "humidity":{
                    "value":str(value),
                    "type":"number"
                    }
                }
        json_data = json.dumps(data)
        print(topic,json_data)
        self.client.publish(topic=topic, msg=json_data)

    def send_status(self,topic):
        data = {
            "status":1
        }
        json_data = json.dumps(data)
        print(topic,json_data)
        self.client.publish(topic=topic, msg=json_data)