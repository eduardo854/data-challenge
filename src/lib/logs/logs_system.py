import logging


def log_manager(name='exemplo',
                log_level='DEBUG',
                log_format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                filename='exemplo.log',
                handler_level='DEBUG'):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level))  # logging.DEBUG
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(filename, encoding='utf8')
    # file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(file_handler)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
