import logging
import time
import threading
import sqlite3
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = 'https://swapi.dev/api/people/'

def get_person(url, cursor):
    response = requests.get(url, timeout=(5, 5))
    if response.status_code == 200:
        person_dict = dict(response.json())
        cursor.execute("INSERT INTO person (name, age, sex) VALUES (?, ?, ?)", (person_dict["name"], person_dict["birth_year"], person_dict["gender"],))

def load_person_in_base(cursor):
    start = time.time()
    for index in range(1, 22):
        get_person(URL + str(index), cursor)
    print("Done in {:4}".format(time.time() - start))

def load_person_in_base_with_threads(cursor):
    start = time.time()
    threads = []
    for index in range(1, 22):
        thread = threading.Thread(target=get_person, args=(URL + str(index), cursor))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Done in {:4}".format(time.time() - start))

if __name__ == "__main__":
    with sqlite3.connect("python.db", check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.executescript("""DROP TABLE IF EXISTS 'person';
                        CREATE TABLE 'person' (
                        name VARCHAR(50),
                        age VARCHAR(50),
                        sex VARCHAR(50));
                        """)
        load_person_in_base_with_threads(cursor)