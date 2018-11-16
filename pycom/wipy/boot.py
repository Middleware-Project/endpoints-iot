from network import WLAN
import machine

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
# Se debe porporcionar la información de otras redes a las que se requiera
# conectar
info = {"PLANOK":"Planok2018.."}

def connect(net):
    wlan.connect(net.ssid, auth=(net.sec, info[net.ssid]), timeout=5000)
    while not wlan.isconnected():
        machine.idle()
    print('WLAN connection succeeded!')

for net in nets:
    if net.ssid == 'PLANOK':
        print('Network found!')
        connect(net)
        break

