from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="order.fanout", exchange_type="fanout")
channel.basic_publish(exchange="order.fanout", routing_key="", body={})
connection.close()
