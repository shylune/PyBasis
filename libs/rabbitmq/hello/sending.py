# -*- coding: utf-8 -*-
# --- author: shi00 ---
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue="hello")
channel.basic_publish(exchange="", routing_key="hello", body="hello rabbit_mq")
print("[x] Sent 'hello rabbit_mq'")
connection.close()
