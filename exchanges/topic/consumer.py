from pika import BlockingConnection, ConnectionParameters


# Get connection instance
connection = BlockingConnection(ConnectionParameters(host="localhost"))
