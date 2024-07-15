

import pika

from configuration import parameters, rabbit_queue_opts

try:
    with pika.BlockingConnection(parameters) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=rabbit_queue_opts["queue"])

        channel.basic_publish(exchange='',
                              routing_key=rabbit_queue_opts["queue"],
                              body=rabbit_queue_opts["message"])

        print(" [x] Sent '" + rabbit_queue_opts['message'] + "!'")
except Exception as e:
    print(str(e), e.__class__.__name__)
