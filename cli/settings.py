'''Application settings'''
import logging
import logging.config
import os

# Logger settings
_APP_NAME = "dracocli"
_LOGGER_LEVEL = "INFO"
_LOGGER_PATH = "/tmp"

_LOGGER_CONFIG = {
    'version': 1,
    'formatters': {
        'stdout': {
            'format': ('[%(levelname)s] %(message)s'),
            'datefmt': None,
        },
        'json_verbose': {
            'format': ('{"timestamp" : "%(asctime)s", "level" : "%(levelname)s", '
                       '"pathname" : "%(pathname)s", "module" : "%(module)s",'
                       '"lineno" : "%(lineno)d", "message" : "%(message)s"}'),
            'datefmt': None,
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'level': _LOGGER_LEVEL,
            'formatter': 'stdout',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(_LOGGER_PATH, '{srv}.log'.format(srv=_APP_NAME)),
            'level': _LOGGER_LEVEL,
            'formatter': 'json_verbose',
            'maxBytes': 104857600,
            'backupCount': 10,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
    },
    'root': {
        'level': _LOGGER_LEVEL,
        'handlers': ['stdout', ],
    },
}


def get_logger():
    """@return logger"""

    logger = logging.getLogger()
    logging.config.dictConfig(_LOGGER_CONFIG)

    return logger
