from mqtt import MQTTClient
from iotmiddleware import IotConnection
import time
import machine
import binascii

# Librerias sensores
from pysense import Pysense
from SI7006A20 import SI7006A20

unique_id = binascii.hexlify(machine.unique_id())
py = Pysense()
si = SI7006A20(py)
connect = IotConnection(str(unique_id),'198.199.68.64')
topic_temperature = "backend/1/1/measures/sensors/temperature"
topic_humidity = "backend/1/1/measures/sensors/humidity"

while True:
    print("Temperature OK")
    connect.send_temperature(topic_temperature,si.temperature(),unique_id)
    time.sleep(10)
    print("Humidity Ok")
    connect.send_humidity(topic_humidity,si.humidity(),unique_id)
    time.sleep(10)