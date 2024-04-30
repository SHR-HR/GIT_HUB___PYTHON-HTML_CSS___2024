import psycopg2
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

try:
    # Подключение к базе данных
    connect = psycopg2.connect(
        dbname="LESSON_№4_29.04.2024_POSTGRESQL",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )

    with connect.cursor() as cur:
        # Создать таблицу пользователей, если она не существует
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(64)
            )
            """
        )

        # Создать таблицу продуктов, если она не существует
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS products
            (
                product_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id),
                name VARCHAR(100) NOT NULL,
                quantity INTEGER
            )
            """
        )

        connect.commit()

    # Добавить пользователя и его товары
    with connect.cursor() as cur:
        user_name = input("Введите логин: ")
        user_password = input("Введите пароль: ")
        hashed_password = hash_password(user_password)
        products_data = [
            ("Молоко", 2),
            ("Хлеб", 1),
            ("Яйца", 6),
            ("Масло", 1),
            ("Сыр", 2)
        ]
        try:
            cur.execute(
                """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
                RETURNING user_id
                """, (user_name, hashed_password)
            )
            user_id = cur.fetchone()[0]
            cur.executemany(
                """
                INSERT INTO products (user_id, name, quantity)
                VALUES (%s, %s, %s)
                """, [(user_id, name, quantity) for name, quantity in products_data]
            )
            connect.commit()
        except psycopg2.errors.UniqueViolation as error:
            print("Пользователь с таким никнеймом уже существует!")
            connect.rollback()

    # Получить пользователя и его товары
    with connect.cursor() as cur:
        login = input("Введите ваш логин: ")
        password = input("Введите ваш пароль: ")
        hashed_password = hash_password(password)
        cur.execute(
            """
            SELECT u.username, p.name, p.quantity
            FROM users u
            JOIN products p ON u.user_id = p.user_id
            WHERE u.username = %s AND u.password = %s
            """, (login, hashed_password)
        )
        user_products = cur.fetchall()

        if not user_products:
            print("Не верные данные!")
        else:
            print("Вы вошли в систему!")
            total_quantity = sum(product[2] for product in user_products)
            print("Товары пользователя:")
            for product in user_products:
                print(f"Название: {product[1]}, Количество: {product[2]}")
            print(f"Общее количество купленных товаров: {total_quantity}")

    # Закрыть подключение к базе данных
    connect.close()

except psycopg2.Error as e:
    print("Ошибка при подключении к базе данных:", e)

























# import psycopg2
# import hashlib
#
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()
#
# try:
#     # Подключение к базе данных
#     connect = psycopg2.connect(
#         dbname="LESSON_№4_29.04.2024_POSTGRESQL",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
#     )
#
#     # Создать таблицу пользователей, если она не существует
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS users
#             (
#                 user_id SERIAL PRIMARY KEY,
#                 username VARCHAR(100) UNIQUE NOT NULL,
#                 password VARCHAR(64)
#             )
#             """
#         )
#         connect.commit()
#
#     # Создать таблицу продуктов, если она не существует
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS products
#             (
#                 product_id SERIAL PRIMARY KEY,
#                 user_id INTEGER REFERENCES users(user_id),
#                 name VARCHAR(100) NOT NULL,
#                 quantity INTEGER
#             )
#             """
#         )
#         connect.commit()
#
#     # Добавить пользователя
#     with connect.cursor() as cur:
#         user_name = input("Введите логин: ")
#         user_password = input("Введите пароль: ")
#         hashed_password = hash_password(user_password)
#         try:
#             cur.execute(
#                 """
#                 INSERT INTO users (username, password) VALUES
#                 (%s, %s) RETURNING user_id
#                 """, (user_name, hashed_password)
#             )
#             user_id = cur.fetchone()[0]
#             connect.commit()
#         except psycopg2.errors.UniqueViolation as error:
#             print("Пользователь с таким никнеймом уже существует!")
#         finally:
#             connect.rollback()
#
#     # Получить всех пользователей
#     with connect.cursor() as cur:
#         cur.execute("SELECT * FROM users")
#         users = cur.fetchall()
#         for user in users:
#             print(f"Name {user[1]}, password {len(user[2])}")
#
#     # Авторизация
#     with connect.cursor() as cur:
#         for _ in range(3):
#             login = input("Введите ваш логин: ")
#             password = input("Введите ваш пароль: ")
#             hashed_password = hash_password(password)
#             cur.execute(
#                 """
#                 SELECT user_id, username FROM users
#                 WHERE username = %s AND password = %s
#                 """, (login, hashed_password)
#             )
#             user = cur.fetchone()
#             if not user:
#                 print("Не верные данные!")
#                 continue
#
#             print("Вы вошли в систему!")
#             break
#
#     # Если пользователь аутентифицирован, добавим несколько товаров для него
#     if user:
#         with connect.cursor() as cur:
#             # Добавляем товары для пользователя
#             products_data = [
#                 ("Молоко", 2),
#                 ("Хлеб", 1),
#                 ("Яйца", 6)
#             ]
#             for product_name, product_quantity in products_data:
#                 cur.execute(
#                     """
#                     INSERT INTO products (user_id, name, quantity)
#                     VALUES (%s, %s, %s)
#                     """, (user[0], product_name, product_quantity)
#                 )
#             connect.commit()
#
#             # Получаем товары пользователя
#             cur.execute(
#                 """
#                 SELECT name, quantity FROM products
#                 WHERE user_id = %s
#                 """, (user[0],)
#             )
#             products = cur.fetchall()
#             print("Товары пользователя:")
#             for product in products:
#                 print(f"Название: {product[0]}, Количество: {product[1]}")
#
#     # Закрыть подключение к базе данных
#     connect.close()
#
# except psycopg2.Error as e:
#     print("Ошибка при подключении к базе данных:", e)




















# import psycopg2
#
# try:
#     # Подключение к базе данных
#     connect = psycopg2.connect(
#         dbname="LESSON_№4_29.04.2024_POSTGRESQL",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
#     )
#
#     # Удаление всех таблиц
#     with connect.cursor() as cur:
#         cur.execute("DROP SCHEMA public CASCADE")
#         cur.execute("CREATE SCHEMA public")
#         connect.commit()
#
#     print("Все таблицы были успешно удалены.")
#
#     # Закрыть подключение к базе данных
#     connect.close()
#
# except psycopg2.Error as e:
#     print("Ошибка при подключении к базе данных:", e)



# import psycopg2
# import hashlib
#
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()
#
# try:
#     # Подключение к базе данных
#     connect = psycopg2.connect(
#         dbname="LESSON_№4_29.04.2024_POSTGRESQL",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
#     )
#
#     # Создать таблицу пользователей, если она не существует
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS users
#             (
#                 user_id SERIAL PRIMARY KEY,
#                 username VARCHAR(100) UNIQUE NOT NULL,
#                 password VARCHAR(64)
#             )
#             """
#         )
#         connect.commit()
#
#     # Создать таблицу продуктов, если она не существует
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS products
#             (
#                 product_id SERIAL PRIMARY KEY,
#                 user_id INTEGER REFERENCES users(user_id),
#                 name VARCHAR(100) NOT NULL,
#                 quantity INTEGER
#             )
#             """
#         )
#         connect.commit()
#
#     # Добавить пользователя
#     with connect.cursor() as cur:
#         user_name = input("Введите логин: ")
#         user_password = input("Введите пароль: ")
#         hashed_password = hash_password(user_password)
#         try:
#             cur.execute(
#                 """
#                 INSERT INTO users (username, password) VALUES
#                 (%s, %s) RETURNING user_id
#                 """, (user_name, hashed_password)
#             )
#             user_id = cur.fetchone()[0]
#             connect.commit()
#         except psycopg2.errors.UniqueViolation as error:
#             print("Пользователь с таким никнеймом уже существует!")
#         finally:
#             connect.rollback()
#
#     # Получить всех пользователей
#     with connect.cursor() as cur:
#         cur.execute("SELECT * FROM users")
#         users = cur.fetchall()
#         for user in users:
#             print(f"Name {user[1]}, password {len(user[2])}")
#
#     # Авторизация
#     with connect.cursor() as cur:
#         for _ in range(3):
#             login = input("Введите ваш логин: ")
#             password = input("Введите ваш пароль: ")
#             hashed_password = hash_password(password)
#             cur.execute(
#                 """
#                 SELECT user_id, username FROM users
#                 WHERE username = %s AND password = %s
#                 """, (login, hashed_password)
#             )
#             user = cur.fetchone()
#             if not user:
#                 print("Не верные данные!")
#                 continue
#
#             print("Вы вошли в систему!")
#             break
#
#     # Получить товары пользователя
#     if user:
#         with connect.cursor() as cur:
#             cur.execute(
#                 """
#                 SELECT name, quantity FROM products
#                 WHERE user_id = %s
#                 """, (user[0],)
#             )
#             products = cur.fetchall()
#             print("Товары пользователя:")
#             for product in products:
#                 print(f"Название: {product[0]}, Количество: {product[1]}")
#
#     # Закрыть подключение к базе данных
#     connect.close()
#
# except psycopg2.Error as e:
#     print("Ошибка при подключении к базе данных:", e)




# import psycopg2

#
# try:
#     # Подключение к базе данных
#     connect = psycopg2.connect(
#         dbname="LESSON_№4_29.04.2024_POSTGRESQL",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
#     )
#
#     # Создание таблицы пользователей, если она не существует
#     with connect.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS users
#             (
#                 user_id SERIAL PRIMARY KEY,
#                 username VARCHAR(100) UNIQUE NOT NULL,
#                 password VARCHAR(100)
#             )
#         """)
#
#     # Запрос логина и пароля у пользователя
#     username = input("СэнПай, укажите пожалуйста Ваш логин: ")
#     password = input("СэнПай, укажите пожалуйста Ваш пароль: ")
#
#     # Добавление пользователя в базу данных
#     with connect.cursor() as cur:
#         try:
#             cur.execute("""
#                 INSERT INTO users (username, password) VALUES (%s, %s)
#             """, (username, password))
#             print("Пользователь успешно добавлен в базу данных.")
#
#             # Вызов метода commit() для сохранения изменений
#             connect.commit()
#
#             # Запрос для получения всех пользователей
#             cur.execute("SELECT * FROM users")
#             users = cur.fetchall()
#             print("Все пользователи в базе данных:")
#             for user in users:
#                 print(user)
#
#         except psycopg2.errors.UniqueViolation as error:
#             print("Ошибка: такой пользователь уже существует.")
#         finally:
#             connect.rollback()
#
#     # Закрытие подключения к базе данных
#     connect.close()
#
# except psycopg2.Error as e:
#     print("Ошибка при подключении к базе данных:", e)






# Вариант 1

#
# import psycopg2
#
#
# with psycopg2.connect(
#     dbname="LESSON_№4_29.04.2024_POSTGRESQL",
#     user="postgres",
#     password="admin",
#     host="localhost",
#     port="5432",
# ) as connect:
#     with connect.cursor() as cur:
#         cur.execute("""
#                     CREATE TABLE IF NOT EXISTS users
#                     (
#                         user_id SERIAL PRIMARY KEY,
#                         username VARCHAR(100) UNIQUE NOT NULL,
#                         password VARCHAR(100)
#                     )
#                     """)
#
#     with connect.cursor() as cur:
#         try:
#             cur.execute("""
#                 INSERT INTO users (username, password) VALUES ('DOOM41', 'qwerty')
#                         """)
#         except psycopg2.errors.UniqueViolation as error:
#             pass
#         finally:
#             connect.rollback()
#
#     with connect.cursor() as cur:
#         a = cur.execute("SELECT * FROM users")
#         users = cur.fetchall()
#         print(users)


# Вариант 2



# import psycopg2

# conn = psycopg2.connect(
#     dbname="LESSON_№4_29.04.2024_POSTGRESQL",
#     user="postgres",
#     password="admin",
#     host="localhost",
#     port="5432"
# )

# cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS users
#             (
#             user_id SERIAL PRIMARY KEY,
#             username VARCHAR(100) UNIQUE NOT NULL,
#             password VARCHAR(100)
#             )
#             """)

# conn.commit()
# cur.close()
# conn.close()
