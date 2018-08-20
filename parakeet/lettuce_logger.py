import logging
import sys
from colorlog import ColoredFormatter
from lettuce import world

from parakeet import next_image

log_level = {'INFO': logging.INFO,
             'WARNING': logging.WARNING,
             'DEBUG': logging.DEBUG,
             'ERROR': logging.ERROR}

APP_LOGGER = 'google.tests.e2e'
SNAPSHOT_DEBUG = 'SNAPSHOT_DEBUG'

formatter_normal = logging.Formatter("[%(processName)s] %(asctime)s - %(name)s - %(levelname)-8s - %(message)s",
                                     datefmt=None)
formatter_color = ColoredFormatter(
        "%(bold_blue)s[%(processName)s]%(reset)s %(green)s%(asctime)s - %(name)s -%(reset)s "
        "%(log_color)s%(levelname)-8s%(reset)s - %(purple)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'blue',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
        }
    )


class CustomLogging(logging.getLoggerClass()):
    """
    The ideia is override our custom logs and do some additional stuffs.
    """
    def debug(self, msg, *args, **kwargs):
        if world.browser.snapshot_debug:
            world.browser.selenium.save_screenshot(
                'parakeet_debug_{:05d}.png'.format(next_image()))
        return super(CustomLogging, self).debug(msg, *args, **kwargs)


def init_logs(level='INFO', logger=None, color_log=False):
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
    ch.setFormatter(formatter_color if color_log else formatter_normal)
    handler.addHandler(ch)


def get_logger():
    """
    Return the default logger.
    :return:
    """
    logging.setLoggerClass(CustomLogging)
    return logging.getLogger(APP_LOGGER)


LOG = get_logger()