
import redis as Redis
import paho.mqtt.client as mqtt
import time

import mqtt_config_reader as mcr
import common_reader
from Exceptions import config_exception

redis = None
client = None
reconnect = True

def getTopicFromMsg(message):
    return "bere" #TODO finire

def startListening():
    print("start listening", flush=True)
    pubsub = redis.pubsub()
    pubsub.subscribe('datidb')
    try:
        for message in pubsub.listen():

            # topic = getTopicFromMsg(message)

            client.publish("all", str(message["data"]))
            # client.publish(str(topic), str(message["data"]))
            # print(str(message["data"]), flush=True)

    finally:
        print("Esco")

def connect():
    return client.connect(mcr.mqtt_address, int(mcr.mqtt_port), 60)

def on_connect():
    print("MQTT Connected.", flush=True)

def onDisconnect():
    print("Disconnected", flush=True)
    # if(reconnect): connect()

# def onPublish():
#     print("Published MQTT", flush=True)

def setup():
    # client.on_connect = on_connect
    # client.on_disconnect = onDisconnect
    if connect() != 0: print("Can't connect", flush=True)
    client.loop_start()
    startListening()


def publishMQTT():
    pass

if __name__ == "__main__":
    print("Avvio MQTTHandler", flush=True)
    redis = Redis.Redis(host=common_reader.redis_address, port=common_reader.redis_port)
    client = mqtt.Client()
    setup()
    startListening()