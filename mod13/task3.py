import sqlite3

def log_bird(cursor, bird_name, date_time):
    cursor.execute("INSERT INTO 'birds' (bird_name, date_time) VALUES (?, ?) ", (bird_name, date_time, ))

def check_if_such_bird_already_seen(cursor, bird_name):
    cursor.execute("SELECT COUNT (*) FROM 'birds' WHERE (bird_name = ?)", (bird_name,))
    result = cursor.fetchall()[0][0]
    if result > 0:
        return True
    return False

if __name__ == "__main__":
    with sqlite3.connect("bird.db") as conn:
        cursor = conn.cursor()
        bird_name = 'Чёрная ворона'
        date_time = '2020-06-24T08:11:17'
        #log_bird(cursor, bird_name, date_time)
        print(check_if_such_bird_already_seen(cursor, bird_name))