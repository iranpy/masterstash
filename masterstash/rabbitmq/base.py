import time
import json
import datetime
import logging

from kombu import Connection
from kombu import Queue
from kombu.mixins import ConsumerMixin


logger = logging.getLogger('rabbitmq')

class BaseConsumer(ConsumerMixin):
    def __init__(self, connection_uri, queues, **kwargs):
        self.connection_uri = connection_uri
        self.connection = None
        self.queues = queues

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues,
                         accept=['pickle', 'json'],
                         callbacks=[self.process_task])]

    def process_task(self, body, message):
        raise NotImplementedError

    def run(self):
        with Connection(self.connection_uri) as self.connection:
            try:
                logger.info("consumer has started on queue %s ..." % self.queues)
                super(BaseConsumer, self).run()
            except KeyboardInterrupt:
                print('exit by ctrl-c')
