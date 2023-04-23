import sqlite3
import csv

def delete_wrong_fees(cursor, wrong_fees_file):
    with open(wrong_fees_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for line in reader:
            cursor.execute('DELETE FROM table_fees WHERE (truck_number = ?) AND (timestamp = ?)', (line[0], line[1], ))

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        wrong_fees_file = 'wrong_fees.csv'
        delete_wrong_fees(cursor, wrong_fees_file)