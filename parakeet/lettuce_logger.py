import logging
import sys
from colorlog import ColoredFormatter

log_level = {'INFO': logging.INFO,
             'WARNING': logging.WARNING,
             'DEBUG': logging.DEBUG,
             'ERROR': logging.ERROR}

APP_LOGGER = 'google.tests.e2e'

formatter = ColoredFormatter(
        "%(green)s%(asctime)s - %(name)s -%(reset)s %(log_color)s%(levelname)-8s%(reset)s"
        " - %(white)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
        }
    )


def init_logs(level='INFO', logger=None):
    """
    Setup the logs inside of the tests.
    :param level:
    :param logger:
    :return:
    """
    handler = logging.getLogger(logger)
    _level = log_level.get(level, logging.INFO)
    handler.setLevel(_level)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(_level)
    ch.setFormatter(formatter)
    handler.addHandler(ch)


def get_logger():
    """
    Return the default logger.
    :return:
    """
    return logging.getLogger(APP_LOGGER)


LOG = get_logger()