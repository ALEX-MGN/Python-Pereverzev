import logging

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
            "level": "INFO",
            "formatter": "base",
        }
    },
    "loggers": {
        "logger": {
            "level": "INFO",
            "handlers": ["file"],
        }
    }
}