
from kombu import Exchange, Queue
task_exchange = Exchange('first_exchange', type='direct')

WORKERS = {
    'finalized_order': {'connection_uri':'amqp://admin:admin@localhost:5672//', 
              'queues': [Queue('fake', task_exchange, routing_key='first_routing_key')]
              }
}

LOGGING = {
        'default_level': 'INFO',
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
                    'base': {
                        'format': '%(asctime)s %(levelname)s %(name)s: %(message)s'
                        },
                    },
        'handlers': {
                    'null': {
                        'class': 'logging.NullHandler',
                    },
                    'console': {
                        'class': 'logging.StreamHandler',
                        'formatter': 'base',
                        'level': 'INFO',
                    },
                    # 'sentry': {
                    #     'class': 'masterstash.logging.MasterstashSentryHandler',
                    #     'level': 'ERROR',
                    #     'tags' : {'names': 'masterstash'},
                    #     'client' : 'sentry-access-address'
                    # }
                },

        'loggers': {
                    'order': {
                        'handlers': ['console'],
                        'propagate': False,
                        'level': 'INFO',
                    },
                    'rabbitmq': {
                        'handlers': ['console'],
                        'level': 'INFO',
                        'propagate': False,
                    },
                    'cli': {
                        'handlers': ['console'],
                        'level': 'INFO',
                        'propagate': False,
                    }
        }
    }