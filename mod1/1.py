from flask import Flask
import random
import datetime
import re, os
app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

carsList = ["Chevrolet", "Renault", "Ford", "Lada"]
@app.route('/cars')
def cars():
    return ", ".join(carsList)

catsList = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
@app.route('/cats')
def cats():
    return random.choice(catsList)

@app.route('/get_time/now')
def get_time_now():
    return '«Точное время: %s»' % (str(datetime.datetime.now()))

@app.route('/get_time/future')
def get_time_future():
    return '«Точное время через час будет %s»' % (str(datetime.datetime.now() + datetime.timedelta(hours=1)))

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt') 

def getwords():
    with open(BOOK_FILE) as book:
        return book.read().split()
bookWords = getwords()
@app.route('/get_random_word')
def get_random_word():
    return re.sub(r'[^а-яА-Яa-zA-Z\s]','', random.choice(bookWords)) 

counter = 0
@app.route('/counter')
def count():
    global counter 
    counter += 1
    return str(counter)

if __name__ == '__main__':
    app.run(debug=True)