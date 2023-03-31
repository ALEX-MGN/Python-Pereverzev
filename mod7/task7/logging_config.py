import logging
class ASCIIFilter(logging.Filter):
    def filter(self, record):
        return str.isascii(record.getMessage())

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "filters": {
        "ascii_filter": {
            "()": ASCIIFilter
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "utils.log",
            'when': 's',
            'interval': 10,
            'backupCount': 1,
            "level": "INFO",
            "formatter": "base",
            "filters": ["ascii_filter"],
        }
    },
    "loggers": {
        "logger": {
            "level": "INFO",
            "handlers": ["file"],
        }
    }
}