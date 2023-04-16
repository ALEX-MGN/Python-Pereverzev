import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_3_database.db") as conn:
        cursor = conn.cursor()

        quantity_str = []
        cursor.execute("SELECT COUNT (id) FROM table_1")
        quantity_str.append(cursor.fetchall()[0][0])
        cursor.execute("SELECT COUNT (id) FROM table_2")
        quantity_str.append(cursor.fetchall()[0][0])
        cursor.execute("SELECT COUNT (id) FROM table_3")
        quantity_str.append(cursor.fetchall()[0][0])
        print(f"Таблица 1 - {quantity_str[0]} записей,таблица 2 - {quantity_str[1]} записей, таблица 3 - {quantity_str[2]} записей")

        cursor.execute("SELECT COUNT(*) FROM (SELECT DISTINCT * FROM table_1)")
        result = cursor.fetchall()[0][0]
        print(f"Уникальных записей в 1 таблице {result}")

        cursor.execute("SELECT COUNT(*) FROM (SELECT * FROM table_1 INTERSECT SELECT * FROM table_2)")
        result = cursor.fetchall()[0][0]
        print(f"Количество записей из 1 таблицы встречается во 2 - {result} запись")

        cursor.execute("SELECT COUNT(*) FROM (SELECT * FROM table_1 INTERSECT SELECT * FROM table_2 INTERSECT SELECT * FROM table_3)")
        result = cursor.fetchall()[0][0]
        print(f"Количество записей из 1 таблицы встречается во 2 и 3 - {result} запись")