from pika import BlockingConnection, ConnectionParameters


def get_connection():
    return BlockingConnection(ConnectionParameters(host="localhost"))
