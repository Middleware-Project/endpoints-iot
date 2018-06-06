from mqtt import MQTTClient
from iotmiddleware import IotConnection
import time
import machine

# Librerias sensores
from pysense import Pysense
from SI7006A20 import SI7006A20

py = Pysense()
si = SI7006A20(py)
connect = IotConnection("pycom1",'198.199.68.64')
topic_temperature = "backend/1/1/measures/sensors/temperature"
topic_humidity = "backend/1/1/measures/sensors/humidity"

while True:
    print("Temperature OK")
    connect.send_temperature(topic_temperature,si.temperature())
    time.sleep(10)
    print("Humidity Ok")
    connect.send_humidity(topic_humidity,si.humidity())
    time.sleep(10)