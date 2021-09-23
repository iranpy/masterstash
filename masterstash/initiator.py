from masterstash.settings import settings

def logger_initiator():
    import logging.config
    logging.config.dictConfig(settings.LOGGING)
