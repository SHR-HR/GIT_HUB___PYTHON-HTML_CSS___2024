# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 29 АПРЕЛЯ 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                              Домашнее задание

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                            Дисциплина: Теория баз данных. PostgreSQL

                                            Домашнее задание №4:

                                        👇🏻 Выполните следующие задания:

👉🏻 1. Удаление пользователя: Добавьте функционал для удаления пользователя из базы данных. 
После получения всех пользователей, спросите у пользователя, какого пользователя они хотели бы удалить,
и удалите его из базы данных.

👉🏻 2. Обновление пароля пользователя: Позвольте пользователям обновлять свои пароли. 
Спросите у пользователя логин и новый пароль, затем обновите пароль соответствующего пользователя в базе данных.

👉🏻 3. Проверка сложности пароля: перед тем, как добавить пользователя, проверьте,
является ли пароль достаточно безопасным. Например, проверьте длину пароля и его сложность 
(наличие букв верхнего и нижнего регистра, цифр и специальных символов).

👉🏻 4. Автоматическая генерация пароля: предложите пользователю сгенерировать надежный пароль,
если они не предоставили свой пароль. Используйте модуль `secrets` для безопасной генерации случайных паролей.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Код из архива к текущему домашнему заданию:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #

import psycopg2


with psycopg2.connect(
    dbname="lesson_third",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
) as connect:
    # Создать таблицу
    with connect.cursor() as cur:
        cur.execute(
            """
                    CREATE TABLE IF NOT EXISTS users 
                    (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(100) UNIQUE NOT NULL,
                        password VARCHAR(100)
                    )
                    """
        )
        connect.commit()

    # Добавить юзера
    with connect.cursor() as cur:
        user_name = input("Введите логин: ")
        user_password = input("Введите пароль: ")
        try:
            cur.execute(
                f"""
                INSERT INTO users (username, password) VALUES 
                ('{user_name}', '{user_password}')
                        """
            )
            connect.commit()
        except psycopg2.errors.UniqueViolation as error:
            print("Пользователь с таким никнеймом уже существует!")
        finally:
            connect.rollback()

    # Получить всех юзеров
    with connect.cursor() as cur:
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        for user in users:
            print(f"Name {user[1]}, password {len(user[2])}")

    # Авторизация
    with connect.cursor() as cur:
        for _ in range(3):
            login = input("Введите ваш логин: ")
            password = input("Введите ваш пароль: ")
            cur.execute(
                f"""
                        SELECT username, password FROM users
                        WHERE username = '{login}' AND password = '{password}'
                """
            )
            user = cur.fetchone()
            if not user:
                print("Не верные данные!")
                continue

            print("Вы вошли в систему!")
            break
            
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 29.04.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import psycopg2
import hashlib
import string
import secrets
import logging

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True

def generate_random_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def add_new_user(cur):
    user_name = input("Введите логин: ")
    user_password = input("Введите пароль: ")
    if not user_password:
        user_password = generate_random_password()
        print("Сгенерирован случайный пароль:", user_password)
    while not check_password_strength(user_password):
        print("Пароль слишком слабый. Пароль должен содержать как минимум 8 символов, включая заглавные и строчные буквы, цифры и специальные символы.")
        user_password = input("Введите пароль: ")
    hashed_password = hash_password(user_password)
    products_data = [
        ("Молоко", 2),
        ("Хлеб", 1),
        ("Яйца", 6),
        ("Масло", 1),
        ("Помидоры", 10),
        ("Огурцы", 5),
        ("Банан", 4),
        ("Мороженое", 3),
        ("Клубника", 9),
        ("Сливки", 69),
        ("Колбаса", 7),
        ("Йогурт", 4),
        ("Дыня", 2),
        ("Арбуз", 2),
        ("Минералка", 10),
        ("Пивас", 25),
        ("Чай Черный", 100),
        ("Чай Зеленый", 50),
        ("Сыр", 12),
        ("Кефир", 7),
        ("Редис", 10),
        ("Лук", 5),
        ("Лук Репчатый", 3),
        ("Конфеты", 2)
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
        print("Пользователь успешно добавлен.")
    except psycopg2.errors.UniqueViolation as error:
        print("Пользователь с таким никнеймом уже существует!")
        connect.rollback()

def delete_user(cur):
    # Получить всех пользователей
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    print("Список всех пользователей:")
    for user in users:
        print(user)

    # Запросить пользователя, которого нужно удалить
    username_to_delete = input("Введите имя пользователя, которого вы хотите удалить: ")

    # Проверить наличие записей в таблице products для удаляемого пользователя
    cur.execute(
        """
        SELECT COUNT(*) FROM products
        WHERE user_id = (SELECT user_id FROM users WHERE username = %s)
        """, (username_to_delete,)
    )
    product_count = cur.fetchone()[0]

    if product_count > 0:
        delete_products = input("У пользователя есть продукты. Желаете удалить их? (Да/Нет): ").lower()
        if delete_products == 'да':
            try:
                cur.execute(
                    """
                    DELETE FROM products
                    WHERE user_id = (SELECT user_id FROM users WHERE username = %s)
                    """, (username_to_delete,)
                )
                print("Продукты пользователя успешно удалены.")
            except psycopg2.Error as error:
                print("Ошибка при удалении продуктов пользователя:", error)
                connect.rollback()
        else:
            print("Продукты пользователя не будут удалены.")

    # Удалить пользователя
    try:
        cur.execute(
            """
            DELETE FROM users
            WHERE username = %s
            """, (username_to_delete,)
        )
        print("Пользователь успешно удален.")
    except psycopg2.Error as error:
        print("Ошибка при удалении пользователя:", error)
        connect.rollback()

def update_password(cur):
    # Запросить пользователя, для которого нужно обновить пароль
    username_to_update = input("Введите имя пользователя, для которого вы хотите обновить пароль: ")

    # Запросить новый пароль
    new_password = input("Введите новый пароль: ")
    hashed_new_password = hash_password(new_password)

    # Обновить пароль пользователя
    try:
        cur.execute(
            """
            UPDATE users
            SET password = %s
            WHERE username = %s
            """, (hashed_new_password, username_to_update)
        )
        print("Пароль пользователя успешно обновлен.")
    except psycopg2.Error as error:
        print("Ошибка при обновлении пароля пользователя:", error)
        connect.rollback()

def list_all_users(cur):
    # Получить всех пользователей
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    print("Список всех пользователей:")
    for user in users:
        print(user)

    # Запросить пользователя, продукты которого нужно показать
    username_to_show_products = input("СэнПай! Не хотите ли Вы увидеть список продуктов - пользователя, которого Вы выбрали из нашего списка? Введите его имя (или введите 'нет'): ")
    if username_to_show_products.lower() != 'нет':
        cur.execute(
            """
            SELECT u.username, p.name, p.quantity
            FROM users u
            JOIN products p ON u.user_id = p.user_id
            WHERE u.username = %s
            """, (username_to_show_products,)
        )
        user_products = cur.fetchall()
        if user_products:
            print(f"Продукты пользователя {username_to_show_products}:")
            for product in user_products:
                print(f"Название: {product[1]}, Количество: {product[2]}")
        else:
            print("Пользователь с таким именем не найден или у него нет продуктов.")

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

        # Установка уровня логирования и формата сообщений
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        while True:
            choice = input("Желаете добавить нового пользователя? (Да/Нет): ").lower()
            if choice == 'да':
                add_new_user(cur)
            elif choice == 'нет':
                choice = input("СэнПай, не желаете ли Вы увидеть весь список пользователей? (Да/Нет): ").lower()
                if choice == 'да':
                    list_all_users(cur)
                    choice = input("Хотите отредактировать пользователя? (Да/Нет): ").lower()
                    if choice == 'да':
                        update_password(cur)
                    choice = input("Хотите удалить пользователя? (Да/Нет): ").lower()
                    if choice == 'да':
                        delete_user(cur)
                elif choice == 'нет':
                    print("До свидания, СэнПай! Запускайте код еще!!!")
                    break
                else:
                    print("Неправильный ввод. Пожалуйста, введите 'Да' или 'Нет'.")
            else:
                print("Неправильный ввод. Пожалуйста, введите 'Да' или 'Нет'.")

except psycopg2.Error as e:
    print("Ошибка при подключении к базе данных:", e)
finally:
    if connect:
        connect.close()
