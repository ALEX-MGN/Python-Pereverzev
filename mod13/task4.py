import sqlite3

def ivan_sovin_the_most_effective(cursor, name):
    global effective_manager
    salary_employee = cursor.execute("SELECT salary FROM 'table_effective_manager' WHERE (name = ?)", (name, )).fetchall()[0][0]

    if effective_manager > salary_employee * 1.1:
        cursor.execute("UPDATE 'table_effective_manager' SET salary = salary * 1.1 WHERE name = ?", (name, ))
    else:
        cursor.execute('DELETE FROM table_effective_manager WHERE name = ? AND name != ?', (name, 'Иван Совин'))

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        effective_manager = cursor.execute("SELECT salary FROM 'table_effective_manager' WHERE (name = 'Иван Совин') ").fetchall()[0][0]
        name = 'Иван Совин'
        ivan_sovin_the_most_effective(cursor, name)