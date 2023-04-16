import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count DESC")
        result = cursor.fetchall()[0][0]
        print(f"Самый популярный цвет: {result}")

        cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Red'")
        red_phones = cursor.fetchall()[0][1]
        cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Blue'")
        blue_phones = cursor.fetchall()[0][1]

        if blue_phones > red_phones:
            print(f"Синих больше на {blue_phones - red_phones}")
        elif blue_phones < red_phones:
            print(f"Красных больше на {red_phones - blue_phones}")
        else:
            print("Количество красных и синих телефонов одинаково")

        cursor.execute("SELECT * FROM table_checkout ORDER BY sold_count")
        result = cursor.fetchall()[0][0]
        print(f"Самый непопулярный цвет: {result}")