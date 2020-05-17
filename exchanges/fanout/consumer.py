from pika import BlockingConnection, ConnectionParameters


def callback(ch, method, properties, payload):
    print(f" [x] {payload}")


connection = BlockingConnection(ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="order.fanout", exchange_type="fanout")
channel.queue_declare(queue="order.cancel", exclusive=True)
channel.queue_bind(exchange="order.fanout", queue="order.cancel")
channel.basic_consume(queue="order.cancel", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
