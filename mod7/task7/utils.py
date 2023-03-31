import logging
import logging.config
from logging_config import dict_config

logging.config.dictConfig(dict_config)

logger = logging.getLogger("logger.logger_calculate")
logger.setLevel("DEBUG")

def plus(number_one, number_two):
    logger.debug(f"Entered worker({number_one},{number_two})")

    result = int(number_one) + int(number_two)
    logger.debug(f"Calculation result of worker({number_one}, {number_two}) = {result}")

    return result

def multiplication(number_one, number_two):
    logger.debug(f"Entered worker({number_one},{number_two})")

    result = int(number_one) * int(number_two)
    logger.debug(f"Calculation result of worker({number_one}, {number_two}) = {result}")

    return result
