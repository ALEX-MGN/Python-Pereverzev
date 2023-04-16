import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_4_database.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT (*) FROM salaries WHERE (salary < 5000)")
        result = cursor.fetchall()[0][0]
        print(f"За чертой бедности: {result}")

        cursor.execute("SELECT AVG(salary) FROM salaries")
        result = cursor.fetchall()[0][0]
        print(f"Средняя зарплата: {result}")

        cursor.execute("SELECT salary FROM salaries ORDER BY salary")
        array = cursor.fetchall()
        result = array[(len(array) + 1) // 2][0]
        print(f"Медианная зарплата: {result}")

        cursor.execute("SELECT COUNT (*) FROM salaries")
        total = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {total})")
        T = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT SUM(salary) - {T} FROM salaries")
        K = cursor.fetchall()[0][0]
        result = round(T / K, 2) * 100
        print(f"Число социального неравенства: F = {result}%")
