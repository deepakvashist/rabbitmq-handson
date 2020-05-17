from pika import BlockingConnection, ConnectionParameters


# Get connection instance
connection = BlockingConnection(ConnectionParameters(host="localhost"))

# Create the connection channel
channel = connection.channel()

# Declare the exchange (idempotent operation)
channel.exchange_declare(exchange="order", exchange_type="direct")

# Declare queue
channel.queue_declare(queue="order.create", exclusive=True)

# Bind queue
channel.queue_bind(exchange="order", routing_key="create", queue="order.create")


def callback(channel, method, properties, payload):
    pass


# Run consumer
channel.basic_consume(queue="order.create", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
