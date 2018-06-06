from network import WLAN
import machine

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
info = {"VTR-7952038":"w5hvTrzbwgrh","CDT":"Planok2012..","TP-LINK_87AEDA":"78479777"}

def connect(net):
    wlan.connect(net.ssid, auth=(net.sec, info[net.ssid]), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
    print('WLAN connection succeeded!')

for net in nets:
    if net.ssid == 'VTR-7952038' or net.ssid == 'CDT' or net.ssid == 'TP-LINK_87AEDA':
        print('Network found!')
        connect(net)
        break
