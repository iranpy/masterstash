import time
import json
import datetime
import logging

from kombu import Connection
from kombu import Queue
from kombu.utils.debug import setup_logging

from masterstash.order.serialization import FinalizedOrderSchema
from masterstash.rabbitmq.base import BaseConsumer
from masterstash.settings import settings


logger = logging.getLogger('order')

class FinalizedOrderConsumer(BaseConsumer):
    def process_task(self, body, message):
        try:
            body = FinalizedOrderSchema().dump(body)
            self.out_sink(body)
        except Exception as exc:
            logger.error('task raised exception: %r', exc)
        message.ack()

    def out_sink(self, body):
        logger.info('loggers %s' % body)
