# RabbitMQ hands on

The purpose of this project is to put it into practice RabbitMQ/AMQP concepts.

## Concepts

#### Exchange

Receives messages from producers and pushes them to queues depending on rules defined by the exchange type. To receive messages, a queue needs to be bound to at least one exchange.

- **Direct:** The message is routed to the queues whose binding key exactly matches the routing key of the message.
- **Fanout:** A fanout exchange routes messages to all of the queues bound to it.
- **Topic:** The topic exchange does a wildcard match between the routing key and the routing pattern specified in the binding.
- **Headers:** Headers exchanges use the message header attributes for routing.

#### Binding

A binding is a link between a queue and an exchange.

#### Routing key

A key that the exchange looks at to decide how to route the message to queues. Think of the routing key like an address for the message.

#### Vhost, virtual host

Provides a way to segregate applications using the same RabbitMQ instance. Different users can have different permissions to different vhost and queues and exchanges can be created, so they only exist in one vhost.
