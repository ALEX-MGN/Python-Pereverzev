import sqlite3
def check_if_vaccine_has_spoiled(cursor, truck_number):
    cursor.execute(f'SELECT COUNT (*) FROM table_truck_with_vaccine WHERE (truck_number = ?) AND NOT(temperature_in_celsius BETWEEN 16 and 20)', (truck_number,))
    result = cursor.fetchall()[0][0]
    if result >= 3:
        return True
    return False

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        #truck_number = "к584тс778"
        truck_number = input()
        print(check_if_vaccine_has_spoiled(cursor, truck_number))