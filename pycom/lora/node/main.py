from network import LoRa
#from iotmiddleware import IotConnection
import socket
import binascii
import struct
import time
import config
import machine
import ujson

# Librerias sensores
from pysense import Pysense
from SI7006A20 import SI7006A20

py = Pysense()
si = SI7006A20(py)

# initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('260213CE'))[0]
nwk_swkey = binascii.unhexlify('75C6693832611BE411392E4038E7C49B')
app_swkey = binascii.unhexlify('C8C566468F877992625D3D8DA84896C3')

# remove all the channels
for channel in range(0, 72):
    lora.remove_channel(channel)

# set all channels to the same frequency (must be before sending the OTAA join request)
for channel in range(0, 72):
    lora.add_channel(channel, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=3)

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))
lora.set_battery_level(0)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

for i in range (200):
    pkt = b'PKT #' + bytes([i])
    value = "%.2f" % (si.temperature())
    data = {
        "value":value
    }

    # data = str(data)
    data = ujson.dumps(data)
    print('Sending:', data)
    s.send(data)
    time.sleep(10)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(6)

