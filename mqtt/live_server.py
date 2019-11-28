import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'

import django

django.setup()

import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#") -> Este subscribe me hace escuchar cosas de sistema
    # Realizar las subscripciones aca por si se desconecta
    client.subscribe("PROD/#")
    client.subscribe("casa/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_message_prod(client, userdata, msg):
    print ("PROD " + msg.topic + " " + str(msg.payload))

    # HACER LO QUE CORRESPONDA


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('eduardo_n', 'eduardo_n')
# Con esto diferenciamos los callback por topic, si no coincide se va a on_message
client.message_callback_add('PROD/#', on_message_prod)
client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
