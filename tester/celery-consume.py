from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue


class MyConsumerStep(bootsteps.ConsumerStep):
    queue = Queue('default', Exchange('default'), 'default')

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[self.queue],
                         callbacks=[self.handle_message],
                         accept=['pickle', 'json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()

# TODO: Use env variables for RabbitMQ credentials
app = Celery(broker='amqp://guest:guest@rabbit//')
app.steps['consumer'].add(MyConsumerStep)
