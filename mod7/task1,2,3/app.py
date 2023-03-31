import sys

from utils import *
from custom_handler import *

logger = logging.getLogger("skillbox")

ch = MultiFileHandler()
logger.addHandler(ch)

#1-2
custom_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(custom_handler)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s", datefmt='%H:%M:%S')
custom_handler.setFormatter(formatter)

def calculate():
    action = input("Напишите дейтсвие: Умножить/Сложить ")
    number_one = input("Введите число 1: ")
    number_two = input("Введите число 2: ")

    if(action != "умножить" and action != "Умножить" and action != "сложить" and action != "Сложить"):
        logger.error("Некорректное действие")
        return "Некорректное действие"
    try:
        number_one = int(number_one)
        number_two = int(number_two)
    except:
        pass
    if(not isinstance(number_one, int)):
        logger.error("Число 1 не явлвяется int")
        return "Число 1 не явлвяется int"
    if(not isinstance(number_two, int)):
        logger.error("Число 2 не явлвяется int")
        return "Число 2 не явлвяется int"

    if(action == "умножить" or action == "Умножить"):
        return multiplication(number_one, number_two)
    elif (action == "сложить" or action == "Сложить"):
        return plus(number_one, number_two)

if __name__ == "__main__":
    print(calculate())