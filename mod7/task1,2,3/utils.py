import logging
import sys
from custom_handler import *

logger = logging.getLogger("logger_calculate")
logger.setLevel("DEBUG")

ch = MultiFileHandler()
logger.addHandler(ch)

#1-2
custom_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(custom_handler)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s", datefmt='%H:%M:%S')
custom_handler.setFormatter(formatter)

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
