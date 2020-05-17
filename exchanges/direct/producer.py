from pika import BlockingConnection, ConnectionParameters


# Get connection instance
connection = BlockingConnection(ConnectionParameters(host="localhost"))

# Create the connection channel
channel = connection.channel()

# Declare the exchange (idempotent operation)
channel.exchange_declare(exchange="order", exchange_type="direct")

# Publish sample message
channel.basic_publish(exchange="order", routing_key="create", body={})
