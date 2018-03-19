# -*- coding: utf-8 -*-
# --- author: slin ---
import pika


def callback(channel, method, properties, body):
    print("[x] Received %r" % body)


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")
channel.basic_consume(callback, queue="hello", no_ack=True)
print("[*] Waiting for message. To exit press CTRL + C")
channel.start_consuming()


