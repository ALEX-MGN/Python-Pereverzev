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
    "handlers": {
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "utils.log",
            'when': 's',
            'interval': 10,
            'backupCount': 1,
            "level": "DEBUG",
            "formatter": "base",
        },
        "server": {
            "class": "logging.handlers.HTTPHandler",
            "level": "DEBUG",
            "host": "localhost:5000",
            "url": "/save_log",
            "method": "POST",
        },
    },
    "loggers": {
        "logger": {
            "level": "DEBUG",
            "handlers": ["file", "server"],
        }
    }
}