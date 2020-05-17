from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="order.direct", exchange_type="direct")
channel.basic_publish(exchange="order.direct", routing_key="create", body={})
