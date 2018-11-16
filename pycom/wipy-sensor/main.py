import time

# Librerias sensores
from pysense import Pysense
from SI7006A20 import SI7006A20

py = Pysense()
si = SI7006A20(py)

while True:
    print("Temperature")
    print("value", si.temperature())
    time.sleep(10)
    print("Humidity")
    print("value", si.humidity())
    time.sleep(10)