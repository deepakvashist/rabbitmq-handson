from pika import BlockingConnection, ConnectionParameters


def callback(channel, method, properties, payload):
    print(f" [x] {payload}")


connection = BlockingConnection(ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="order.direct", exchange_type="direct")
channel.queue_declare(queue="order.create", exclusive=True)
channel.queue_bind(exchange="order.direct", routing_key="create", queue="order.create")
channel.basic_consume(queue="order.create", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
