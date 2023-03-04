from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

weekday = datetime.today().weekday()
weekdays = ["Хорошего понедельника!","Хорошего вторника!","Хорошей среды!","Хорошего четверга!","Хорошей пятницы!","Хорошей субботы!","Хорошего воскресенья!"]
@app.route("/hello-world/<username>")
def hello_world(username):
    return f'Привет, {username}. {weekdays[weekday]}'

@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    for number in numbers.split("/"):
        try:
            int(number)
        except:
            return 'Вы ввели не число'
    return f'Максимальное число: <i>{max(map(int, numbers.split("/")))}</i>'

base_dir = os.path.dirname(os.path.abspath(__file__))
@app.route("/preview/<int:size>/<path:relative_path>")
def file_preview(size, relative_path):
    abs_path = os.path.join(base_dir, relative_path)
    with open(abs_path) as file:
        first_symbols = file.read(size)
    return f'<b>{abs_path}</b> {size} <br> {first_symbols}'


storage = {}
@app.route("/add/<date>/<int:number>")
def save(date, number):
    try:
        storage.setdefault(int(date[0:4]), {}).setdefault(int(date[4:6]), 0)
        storage[int(date[0:4])][int(date[4:6])] += number
    except: 
        return "Неверные значения"
    return "Трата добавлена"

@app.route("/calculate/<int:year>")
def calculateYear(year):
    try:
        storage[year]
    except:
        return f"Значение о {year} годе отсутствуют"
    return str(sum(storage[year].values()))

@app.route("/calculate/<int:year>/<int:month>")
def calculateMounth(year, month):
    try:
        storage[year] and storage[year][month]
    except:
        return f"Значение о {year} годе {month} месяце отсутствуют"
    return str(storage[year][month])

if __name__ == '__main__':
    app.run(debug=True)