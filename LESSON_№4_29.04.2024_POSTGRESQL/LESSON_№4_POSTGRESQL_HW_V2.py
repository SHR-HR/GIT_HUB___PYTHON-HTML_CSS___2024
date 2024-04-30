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

try:
    # Подключение к базе данных
    connect = psycopg2.connect(
        dbname="LESSON_№4_29.04.2024_POSTGRESQL",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )

    # Проверка подключения
    if connect:
        print("Подключение к базе данных успешно.")

    with connect.cursor() as cur:
        # Проверка данных в базе данных
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        if not users:
            print("В базе данных нет пользователей.")
        else:
            print("Список всех пользователей:")
            for user in users:
                print(user)

        while True:
            choice = input("Выберите действие (1 - добавить пользователя, 2 - удалить пользователя, 3 - обновить пароль): ")
            if choice == '1':
                user_name = input("Введите логин: ")
                user_password = input("Введите пароль: ")
                if not user_password:
                    user_password = generate_random_password()
                    print("Сгенерирован случайный пароль:", user_password)
                while not check_password_strength(user_password):
                    print("Пароль слишком слабый. Пароль должен содержать как минимум 8 символов, включая заглавные и строчные буквы, цифры и специальные символы.")
                    user_password = input("Введите пароль: ")
                hashed_password = hash_password(user_password)
                cur.execute(
                    """
                    INSERT INTO users (username, password)
                    VALUES (%s, %s)
                    RETURNING user_id
                    """, (user_name, hashed_password)
                )
                user_id = cur.fetchone()[0]
                products_data = [
                    ("Молоко", 2),
                    ("Хлеб", 1),
                    ("Яйца", 6),
                    ("Масло", 1),
                    ("Сыр", 2)
                ]
                cur.executemany(
                    """
                    INSERT INTO products (user_id, name, quantity)
                    VALUES (%s, %s, %s)
                    """, [(user_id, name, quantity) for name, quantity in products_data]
                )
                print("Пользователь успешно добавлен.")
                break

            elif choice == '2':
                cur.execute("SELECT * FROM users")
                users = cur.fetchall()
                if not users:
                    print("В базе данных нет пользователей для удаления.")
                    break
                print("Список всех пользователей:")
                for user in users:
                    print(user)
                username_to_delete = input("Введите имя пользователя, которого вы хотите удалить: ")
                cur.execute(
                    """
                    DELETE FROM users
                    WHERE username = %s
                    """, (username_to_delete,)
                )
                print("Пользователь успешно удален.")
                break

            elif choice == '3':
                login = input("Введите ваш логин: ")
                old_password = input("Введите ваш старый пароль: ")
                new_password = input("Введите ваш новый пароль: ")
                hashed_old_password = hash_password(old_password)
                hashed_new_password = hash_password(new_password)
                cur.execute(
                    """
                    UPDATE users
                    SET password = %s
                    WHERE username = %s AND password = %s
                    """, (hashed_new_password, login, hashed_old_password)
                )
                if cur.rowcount == 0:
                    print("Не верные данные!")
                else:
                    print("Пароль успешно обновлен.")
                break

            else:
                print("Некорректный ввод. Пожалуйста, выберите действие снова.")

except psycopg2.Error as e:
    print("Ошибка при подключении к базе данных:", e)
finally:
    if connect:
        connect.close()
