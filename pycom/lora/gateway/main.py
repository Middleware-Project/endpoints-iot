import socket
import struct
from network import LoRa 
import time
import machine
import binascii

# MQTT

from mqtt import MQTTClient
from iotmiddleware import IotConnection

connect = IotConnection("pycom1",'198.199.68.64')
unique_id = binascii.hexlify(machine.unique_id())
print(unique_id)
_LORA_PKG_FORMAT = "!BBB%ds"

_LORA_PKG_ACK_FORMAT = "BBBB"

# Open a Lora Socket, use rx_iq to avoid listening to our own messages
lora = LoRa(mode=LoRa.LORA, rx_iq=True)
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_sock.setblocking(False)

while (True):
    # Since the maximum body size in the protocol is 255 the request is limited to 512 bytes
    recv_pkg = lora_sock.recv(512)
    
    # If at least a message with the header is received process it
    if (len(recv_pkg) > 3):
        recv_pkg_len = recv_pkg[1]

        # If message is corrupted should not continue processing
        if (not len(recv_pkg) == recv_pkg_len + 3):
            continue

        # Unpack the message based on the protocol definition
        device_id, pkg_len, msg_id, msg = struct.unpack(_LORA_PKG_FORMAT % recv_pkg_len, recv_pkg)
        print(msg)

        # Respond to the device with an acknoledge package
        # time.sleep(0.15)
        ack_pkg = struct.pack(_LORA_PKG_ACK_FORMAT, device_id, 1, msg_id, 200)
        lora_sock.send(ack_pkg)

        # Do any extra processing required for the package. Keep in mind it should be as fast as posible
        # to make sure that the other clients are not waiting too long for their messages to be acknoleged
