# -*- coding: utf-8 -*-
import time

import pika


def callback(channel, method, properties, body):
    print("****** received: %r" % body)
    time.sleep(body.count(b'.'))


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")
channel.basic_consume(callback, queue="hello", no_ack=True)
print("--- Waiting for message. To exit press ctrl + c. ---")
channel.start_consuming()


