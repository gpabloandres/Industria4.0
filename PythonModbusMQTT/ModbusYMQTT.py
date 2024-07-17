import paho.mqtt.client as mqtt
import time
import random

servidor = "broker.mqtt.cool"
cliente = mqtt.Client(protocol=mqtt.MQTTv5)

cliente.connect(servidor, 1883)

try:
    while True:
        lectura = PLC.read discrete_inputs(0,1)
        estadoEntrada = lectura.bits[0]
        cliente.publish("EntradaPLC",estadoEntrada)
        time.sleep(0.2)
except:
    PLC.close()    


""" Alternativa con random
servidor = “broker.mqtt.cool”
cliente = mqtt.Client(protocol=mqtt.MQTTv5)
cliente.connect(servidor, 1883)
x=0
while True:
x=random.randint(0,20)
cliente.publish(“ingelearn”, x)
time.sleep(0.2)
print(x)
if x==20:
break
"""