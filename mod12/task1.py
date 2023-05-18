import logging
import time
import sqlite3
import requests
import multiprocessing
from multiprocessing.pool import ThreadPool, Pool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = 'https://swapi.dev/api/people/'

def get_person(url):
    with sqlite3.connect("python.db", check_same_thread=False) as conn:
        cursor = conn.cursor()
        response = requests.get(url, timeout=(5, 5))
        if response.status_code == 200:
            person_dict = dict(response.json())
            cursor.execute("INSERT INTO person (name, age, sex) VALUES (?, ?, ?)", (person_dict["name"], person_dict["birth_year"], person_dict["gender"],))

def load_person_in_base_with_pool():
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        start = time.time()
        args = [URL + str(i) for i in range(1, 22)]
        pool.map(get_person, args)

        print("Done in {:4}".format(time.time() - start))

def load_person_in_base_with_threadpool():
    with ThreadPool(processes=multiprocessing.cpu_count() * 5) as pool:
        start = time.time()
        args = [URL + str(i) for i in range(1, 22)]
        pool.map(get_person, args)

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
    load_person_in_base_with_pool()
    load_person_in_base_with_threadpool()