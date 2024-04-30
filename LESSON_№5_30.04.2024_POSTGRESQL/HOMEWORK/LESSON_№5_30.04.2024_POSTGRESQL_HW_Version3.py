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
Вариант кода 3.
'''
import psycopg2
import secrets
import string

# Функция для генерации случайного пароля
def generate_random_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Функция для регистрации обычного пользователя
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
    secret_word = input("Сэнпай! Ты мечтаешь шепнуть мне на ушко \"секретное слово\"???: ")
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

    # Выбор действия: регистрация, авторизация или регистрация суперпользователя
    action = input("Выберите действие: 1 - Сэнпай, ты желаешь пройти регистрацию, чтобы быть в системе???, 2 - Сэнпай, ты хочешь провести авторизацию и войти в систему???, 3 - Сэнпай! Ты мечтаешь шепнуть мне на ушко \"секретное слово\"???: ")

    if action == '1':
        register_user(connect)
    elif action == '2':
        authorize_user(connect)
    elif action == '3':
        register_super_user(connect)
    else:
        print("Неправильный выбор действия.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг №1. - Подключение к базе данных и создание таблицы пользователей
'''
'''
Оглавление: Подключение к базе данных и создание таблицы пользователей
'''
'''
Пример кода:
'''
'''

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
                user_role VARCHAR(100) DEFAULT 'user',
                CONSTRAINT user_role_good CHECK (user_role IN ('user', 'superuser')),
                CONSTRAINT pass_len_check CHECK (LENGTH(user_password) >= 8)
            )
            """
        )
        connect.commit()

'''
'''
Описание: 

В этом блоке кода происходит подключение к базе данных PostgreSQL с использованием библиотеки psycopg2.
Затем создается таблица пользователей, если она еще не существует. 
Таблица содержит следующие поля: user_id (идентификатор пользователя), user_name (имя пользователя), 
user_password (пароль пользователя), user_role (роль пользователя). 
Также устанавливаются ограничения на уникальность имени пользователя и длину пароля.
'''
'''
Шаг №2. - Функция для генерации случайного пароля
'''
'''
Оглавление: Функция для генерации случайного пароля
'''
'''
Пример кода:
'''
'''

def generate_random_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

'''
'''
Описание: 

Эта функция генерирует случайный пароль заданной длины.
Она использует модули secrets и string для создания пароля из случайных символов ASCII (буквы, цифры, знаки пунктуации).
По умолчанию длина пароля равна 20 символам.
'''
'''
Шаг №3. - Функция для регистрации обычного пользователя
'''
'''
Оглавление: Функция для регистрации обычного пользователя
'''
'''
Пример кода:
'''
'''

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
            
'''
'''
Описание: 

Эта функция позволяет обычному пользователю зарегистрироваться в системе. 
Она запрашивает у пользователя логин и пароль, затем проверяет, не занят ли уже указанный логин. 
Если логин свободен и пароль соответствует требованиям (не менее 8 символов), то пользователь добавляется в базу данных.
'''
'''
Шаг №4. - Функция для регистрации суперпользователя
'''
'''
Оглавление: Функция для регистрации суперпользователя
'''
'''
Пример кода:
'''
'''

def register_super_user(connect):
    secret_word = input("Сэнпай! Ты мечтаешь шепнуть мне на ушко \"секретное слово\"???: ")
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

'''
'''
Описание: 

Эта функция позволяет суперпользователю зарегистрировать нового суперпользователя. 
Для этого необходимо ввести секретное слово, после чего вводятся логин и пароль суперпользователя. 
Проверяется уникальность логина и соответствие пароля требованиям.
'''
'''
Шаг №5. - Функция для авторизации пользователя
'''
'''
Оглавление: Функция для авторизации пользователя
'''
'''
Пример кода:
'''
'''

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

'''
'''
Описание: 

Эта функция выполняет авторизацию пользователя. 
Пользователю предлагается ввести логин и пароль, после чего происходит проверка соответствия введенных
данных данным из базы данных. В случае успешной авторизации вызываются действия соответствующего роли пользователя.
'''
'''
Шаг №6. - Функция для действий суперпользователя
'''
'''
Оглавление: Функция для действий суперпользователя
'''
'''
Пример кода:
'''
'''

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

'''
'''
Описание: 

Эта функция обеспечивает действия суперпользователя. 
В цикле предлагается выбрать одно из доступных действий: просмотр пользователей, 
удаление пользователя или выход из режима суперпользователя. В зависимости от выбора вызываются соответствующие функции.
'''
'''
Шаг №7. - Функция для просмотра списка пользователей
'''
'''
Оглавление: Функция для просмотра списка пользователей
'''
'''
Пример кода:
'''
'''

def view_users(connect):
    with connect.cursor() as cur:
        cur.execute("SELECT user_id, user_name, user_role FROM users")
        users = cur.fetchall()
        print("Список пользователей:")
        for user in users:
            print(user)

'''
'''
Описание: 

Эта функция выводит список всех пользователей из базы данных. 
С помощью SQL-запроса выбираются данные о всех пользователях (их идентификаторы, логины и роли),
после чего они выводятся на экран.
'''
'''
Шаг №8. - Функция для удаления пользователя
'''
'''
Оглавление: Функция для удаления пользователя
'''
'''
Пример кода:
'''
'''

def delete_user(connect):
    user_id = input("Введите ID пользователя для удаления: ")
    with connect.cursor() as cur:
        cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        connect.commit()
        print("Пользователь успешно удален.")

'''
'''
Описание: 

Эта функция позволяет суперпользователю удалить пользователя из базы данных. 
Сначала запрашивается идентификатор пользователя, затем выполняется SQL-запрос на удаление пользователя с указанным
идентификатором. 
После выполнения запроса происходит фиксация изменений в базе данных.
'''
'''
Шаг №9. - Функция для действий обычного пользователя
'''
'''
Оглавление: Функция для действий обычного пользователя
'''
'''
Пример кода:
'''
'''

def user_actions(user_id, connect):
    print(f"Доступ к действиям обычного пользователя с ID {user_id}")

'''
'''
Описание: 

Эта функция пока просто выводит сообщение о доступе к действиям обычного пользователя с указанным идентификатором.
В реальном приложении здесь можно было бы добавить логику для выполнения каких-то действий пользователем.
'''
'''
Шаг №10. - Выбор действия и основной поток выполнения программы
'''
'''
Оглавление: Выбор действия и основной поток выполнения программы
'''
'''
Пример кода:
'''
'''

action = input("Выберите действие: 1 - Сэнпай, ты желаешь пройти регистрацию, чтобы быть в системе???, 
2 - Сэнпай, ты хочешь провести авторизацию и войти в систему???, 
3 - Сэнпай! Ты мечтаешь шепнуть мне на ушко \"секретное слово\"???: ")

if action == '1':
    register_user(connect)
elif action == '2':
    authorize_user(connect)
elif action == '3':
    register_super_user(connect)
else:
    print("Неправильный выбор действия.")

'''
'''
Описание: 

В этом блоке кода пользователю предлагается выбрать одно из трех действий: регистрация обычного пользователя, 
авторизация пользователя или регистрация суперпользователя. В зависимости от выбора вызываются соответствующие функции.
'''
