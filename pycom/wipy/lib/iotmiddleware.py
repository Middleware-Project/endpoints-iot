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
        self.client = MQTTClient(client_id,server,port=1883,keepalive=60)
        self.client.set_callback(sub_cb)
        self.client.set_last_will('backend/1/1/status/heartbeat','down',retain=False,qos=0)
        self.client.connect()
        self.client.publish(topic='backend/1/1/status/heartbeat',msg = 'up',qos=1)

    def send_temperature(self,topic,value,unique_id):
        data = {
                    "temperature":{
                    "value":str(value),
                    "unique_id":str(unique_id)
                    }
                }
        json_data = json.dumps(data)
        print(topic,json_data)
        self.client.publish(topic=topic, msg=json_data)

    def send_humidity(self,topic,value,unique_id):
        data = {
                    "humidity":{
                    "value":str(value),
                    "unique_id":str(unique_id)
                    }
                }
        json_data = json.dumps(data)
        print(topic,json_data)
        self.client.publish(topic=topic, msg=json_data)