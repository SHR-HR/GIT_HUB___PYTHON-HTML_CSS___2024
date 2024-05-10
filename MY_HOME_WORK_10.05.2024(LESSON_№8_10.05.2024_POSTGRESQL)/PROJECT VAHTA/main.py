# 10.05.2024 - 11.05.2024.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Чуть-чуть доработал код для его запуска в основном в PyCharm.
# Для того чтобы остановить выполнение запуска кода нажимайте CTRL+F2 (в VS CODE это CTRL+C).
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Домашняя Работа от 03.05.2024 - "Реализовать уход сотрудника".
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Ваш код который Вы Думан скинули нам в чат на уроке (урок от 10.05.2024).

# import psycopg2
# from datetime import datetime
#
# while True:
#     user_id = input("Введите ваш id: ")
#     if not user_id or not user_id.isnumeric():
#         print("Не верные данные")
#         continue
#
#     with psycopg2.connect(
#             dbname="my_vahta",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#     ) as connect:
#         with connect.cursor() as cur:
#             cur.execute(f"SELECT * FROM users WHERE user_id = {user_id};")
#             user = cur.fetchone()
#             if not user:
#                 print("Пользователь с таким id не существует: ")
#                 continue
#
#         # Пришел
#         with connect.cursor() as cur:
#             corrent_time = datetime.now()
#             cur.execute(f"""INSERT INTO work_time (user_id, status, time_into)
#                         VALUES ({user_id}, true, '{corrent_time}')""")








