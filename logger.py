import logging
import os
import platform
import sys
from logging.handlers import RotatingFileHandler

from config import CONFIG

BASE_DIR = os.path.dirname(__file__)

client_name = platform.node()

# Create handlers
c_handler = logging.StreamHandler(sys.stdout)
f_handler = RotatingFileHandler(os.path.join(os.path.join(BASE_DIR, 'logs'), f'{client_name}.log'),
                                maxBytes=10 * 1024 * 1024, backupCount=10, encoding="utf-8")
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter(f'%(asctime)s - {client_name} | %(levelname)s | %(message)s')
f_format = logging.Formatter(f'%(asctime)s - {client_name} | %(levelname)s | %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(c_handler)
logger.addHandler(f_handler)


def log_info(statement):
    if CONFIG.ENABLE_LOGGER:
        logger.info(statement)


def log_error(statement, exc_info=True):
    if CONFIG.ENABLE_LOGGER:
        logger.error(statement, exc_info=exc_info)


def log_critical(statement, exc_info=True):
    if CONFIG.ENABLE_LOGGER:
        logger.critical(statement, exc_info=exc_info)
