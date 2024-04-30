# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ПРАКТИЧЕСКОЙ РАБОТЫ: 29 АПРЕЛЯ 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                            Практическая работа

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                            Дисциплина: Теория баз данных. PostgreSQL

                                            Практическая работа №4
                                       
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 29.04.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
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
