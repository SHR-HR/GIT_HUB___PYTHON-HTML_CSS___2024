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
Вариант кода 1.
'''


import psycopg2
import secrets
import string


def generate_random_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


# Функция для авторизации пользователя
def authorize_user(connect):
    attempts = 3
    while attempts > 0:
        user_name = input("Введите логин: ")
        user_password = input("Введите пароль: ")

        with connect.cursor() as cur:
            cur.execute(
                """
                SELECT user_id FROM users WHERE user_name = %s AND user_password = %s
                """, (user_name, user_password)
            )
            user = cur.fetchone()

            if user:
                print("Авторизация успешна.")
                return True
            else:
                print("Неправильный логин или пароль.")
                attempts -= 1
                print(f"Осталось попыток: {attempts}")

        if attempts == 0:
            print("Превышено количество попыток.")
            return False


# Функция для регистрации нового пользователя
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
                INSERT INTO users (user_name, user_password) VALUES 
                (%s, %s)
                """, (user_name, user_password)
            )
            connect.commit()
            print("Пользователь успешно зарегистрирован.")


# Функция для создания суперпользователя
def create_super_user(connect):
    super_user_name = "super_user"
    super_user_password = generate_random_password()

    with connect.cursor() as cur:
        cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{super_user_name}\';')
        user = cur.fetchone()

        if user:
            print("Суперпользователь уже существует.")
        else:
            cur.execute(
                """
                INSERT INTO users (user_name, user_password, user_role) VALUES 
                (%s, %s, %s)
                """, (super_user_name, super_user_password, "admin")
            )
            connect.commit()
            print("Суперпользователь успешно создан.")
            print("Ваш пароль:", super_user_password)


# Функция для вывода списка всех пользователей и их ID
def list_all_users(connect):
    with connect.cursor() as cur:
        cur.execute("SELECT user_id, user_name FROM users")
        users = cur.fetchall()
        print("Список всех пользователей:")
        for user in users:
            print(f"ID: {user[0]}, Имя: {user[1]}")


# Функция для удаления пользователя по ID
def delete_user_by_id(connect, user_id):
    with connect.cursor() as cur:
        try:
            cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            connect.commit()
            print("Пользователь успешно удален.")
        except psycopg2.Error as e:
            print("Ошибка при удалении пользователя:", e)
            connect.rollback()


# Определение роли пользователя
def determine_user_role(user_name, connect):
    with connect.cursor() as cur:
        cur.execute("SELECT user_role FROM users WHERE user_name = %s", (user_name,))
        user_role = cur.fetchone()
        return user_role[0] if user_role else None


# Подключение к базе данных
with psycopg2.connect(
        dbname="work_db",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
) as connect:
    with connect.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (
                user_id serial PRIMARY KEY,
                user_name VARCHAR(100) UNIQUE NOT NULL,
                user_password VARCHAR(100),
                user_role VARCHAR(100) DEFAULT 'guest',
                CONSTRAINT user_role_good CHECK (user_role IN ('admin', 'user', 'guest')),
                CONSTRAINT pass_len_chek CHECK (LENGTH(user_password) >= 8)
            )
            """
        )
        connect.commit()

    # Выбор между авторизацией и регистрацией
    actions = {
        '1': authorize_user,
        '2': register_user,
    }

    action = input("Выберите действие: 1 - Авторизация, 2 - Регистрация: ")

    if action in actions:
        actions[action](connect)
    else:
        print("Неправильный выбор действия.")

    # Создание суперпользователя
    create_super_user(connect)

    # Получение роли текущего пользователя
    user_name = input("Введите свой логин для определения роли: ")
    user_role = determine_user_role(user_name, connect)

    if user_role == 'admin':
        # Вывод списка пользователей для администратора
        list_all_users(connect)

        # Удаление пользователя по ID для администратора
        user_id_to_delete = input("Введите ID пользователя, которого вы хотите удалить: ")
        delete_user_by_id(connect, user_id_to_delete)
