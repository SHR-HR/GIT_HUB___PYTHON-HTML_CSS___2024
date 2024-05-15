import psycopg2
from datetime import datetime


try:
    while True:
        user_id = input("Введите ваш id: ")
        if not user_id or not user_id.isnumeric():
            print("Не верные данные")
            continue

        with psycopg2.connect(
                dbname="my_vahta",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
        ) as connect:
            with connect.cursor() as cur:
                cur.execute(f"SELECT * FROM users WHERE user_id = {user_id};")
                user = cur.fetchone()
                if not user:
                    print("Пользователь с таким id не существует: ")
                    continue

        # Пришел
        with psycopg2.connect(
                dbname="my_vahta",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
        ) as connect:
            with connect.cursor() as cur:
                current_time = datetime.now()
                cur.execute(f"""INSERT INTO work_time (user_id, status, time_into) 
                            VALUES ({user_id}, true, '{current_time}')""")

except KeyboardInterrupt:
    print("Программа завершена пользователем.")