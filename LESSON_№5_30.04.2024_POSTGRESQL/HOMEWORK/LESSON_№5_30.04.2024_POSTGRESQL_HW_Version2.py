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

                                            Домашнее задание №5:

                                        👇🏻 Выполните следующие задания:

👉🏻 Сделать так чтобы admin мог получать список пользователей и удалять по id определенных.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 30.04.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант кода 2.
'''
import psycopg2
import secrets
import string

# Функция для генерации случайного пароля
def generate_random_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Функция для регистрации пользователя
def register_user(connect):
    user_name = input("Введите логин: ")
    user_password = input("Введите пароль: ")

    with connect.cursor() as cur:
        cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{user_name}\';')
        user = cur.fetchone()

        if user:
            print("Данный никнейм уже занят!")
        elif len(user_password) < 8:
            print("Ваш пароль не может содержать меньше 8 символов!")
        else:
            cur.execute(
                """
                INSERT INTO users (user_name, user_password, user_role) VALUES 
                (%s, %s, %s)
                """, (user_name, user_password, "user")
            )
            connect.commit()
            print("Пользователь успешно зарегистрирован.")

# Функция для регистрации суперпользователя
def register_super_user(connect):
    secret_word = input("Введите секретное слово: ")
    if secret_word == "секретное_слово":
        super_user_name = input("Введите логин суперпользователя: ")
        super_user_password = input("Введите пароль суперпользователя: ")

        with connect.cursor() as cur:
            cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{super_user_name}\';')
            user = cur.fetchone()

            if user:
                print("Суперпользователь уже существует.")
            elif len(super_user_password) < 8:
                print("Пароль суперпользователя не может содержать меньше 8 символов!")
            else:
                cur.execute(
                    """
                    INSERT INTO users (user_name, user_password, user_role) VALUES 
                    (%s, %s, %s)
                    """, (super_user_name, super_user_password, "superuser")
                )
                connect.commit()
                print("Суперпользователь успешно зарегистрирован.")
    else:
        print("Неправильное секретное слово. Регистрация обычного пользователя.")
        register_user(connect)

# Функция для авторизации пользователя
def authorize_user(connect):
    user_name = input("Введите логин: ")
    user_password = input("Введите пароль: ")

    with connect.cursor() as cur:
        cur.execute(
            """
            SELECT user_id, user_role FROM users WHERE user_name = %s AND user_password = %s
            """, (user_name, user_password)
        )
        user = cur.fetchone()

        if user:
            print("Авторизация успешна.")
            user_id, user_role = user
            if user_role == "superuser":
                superuser_actions(connect)
            else:
                user_actions(user_id, connect)
        else:
            print("Неправильный логин или пароль.")

# Функция для действий суперпользователя
def superuser_actions(connect):
    while True:
        action = input("Выберите действие: 1 - Просмотр пользователей, 2 - Удаление пользователя, 3 - Выход: ")

        if action == '1':
            view_users(connect)
        elif action == '2':
            delete_user(connect)
        elif action == '3':
            print("Выход из режима суперпользователя.")
            break
        else:
            print("Неправильный выбор действия.")

# Функция для просмотра списка пользователей
def view_users(connect):
    with connect.cursor() as cur:
        cur.execute("SELECT user_id, user_name, user_role FROM users")
        users = cur.fetchall()
        print("Список пользователей:")
        for user in users:
            print(user)

# Функция для удаления пользователя
def delete_user(connect):
    user_id = input("Введите ID пользователя для удаления: ")
    with connect.cursor() as cur:
        cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        connect.commit()
        print("Пользователь успешно удален.")

# Функция для действий обычного пользователя
def user_actions(user_id, connect):
    print(f"Доступ к действиям обычного пользователя с ID {user_id}")

# Подключение к базе данных
with psycopg2.connect(
        dbname="work_db",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
) as connect:
    # Создание таблицы пользователей, если ее еще нет
    with connect.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (
                user_id serial PRIMARY KEY,
                user_name VARCHAR(100) UNIQUE NOT NULL,
                user_password VARCHAR(100),
                user_role VARCHAR(100) DEFAULT 'user',
                CONSTRAINT user_role_good CHECK (user_role IN ('user', 'superuser')),
                CONSTRAINT pass_len_check CHECK (LENGTH(user_password) >= 8)
            )
            """
        )
        connect.commit()

    # Выбор между регистрацией и регистрацией суперпользователя
    action = input("Выберите действие: 1 - Регистрация, 2 - Регистрация суперпользователя: ")

    if action == '1':
        register_user(connect)
    elif action == '2':
        register_super_user(connect)
    else:
        print("Неправильный выбор действия.")

    # Авторизация пользователя
    authorize_user(connect)
