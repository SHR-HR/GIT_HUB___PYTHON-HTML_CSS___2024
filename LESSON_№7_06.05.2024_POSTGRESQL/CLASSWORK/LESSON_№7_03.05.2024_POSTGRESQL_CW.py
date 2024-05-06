



















# import psycopg2
#
# try:
#     connection = psycopg2.connect(
#         database="postgres",
#         host="localhost",
#         user="postgres",
#         password="admin",
#         port="5432"
#     )
#
#     cursor = connection.cursor()
#
#     # Создание таблицы, если она не существует
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS users_12345 (
#             id SERIAL PRIMARY KEY,
#             login VARCHAR(32) NOT NULL,
#             password VARCHAR(32) NOT NULL,
#             balance DECIMAL
#         );
#     """
#     cursor.execute(create_table_query)
#     connection.commit()
#
#     # Начало транзакции
#     cursor.execute("BEGIN;")
#
#     # Добавление пользователя
#     insert_query = """
#         INSERT INTO users_12345 (login, password, balance)
#         VALUES ('first_user', '12345', 0.0);
#     """
#     cursor.execute(insert_query)
#
#     # Пример транзакции с несколькими действиями
#     transaction_query = """
#         INSERT INTO users_12345 (login, password, balance)
#         VALUES ('second_user', '0123456789', 0.0);
#
#         UPDATE users_12345 SET balance = balance + 1000 WHERE login='second_user';
#         UPDATE users_12345 SET balance = balance + 500 WHERE login='first_user';
#         UPDATE users_12345 SET balance = balance - 500 WHERE login='second_user';
#     """
#     cursor.execute(transaction_query)
#
#     # Пример отката транзакции
#     rollback_query = """
#         UPDATE users_12345 SET login = 'changed_login'
#         WHERE login='first_user';
#     """
#     cursor.execute(rollback_query)
#     connection.rollback()
#
#     # Получение данных пользователей
#     get_users_query = "SELECT * FROM users_12345;"
#     cursor.execute(get_users_query)
#     data = cursor.fetchall()
#     print(data)
#
#     # Конец транзакции
#     connection.commit()
# except psycopg2.Error as e:
#     connection.rollback()
#     print("Ошибка работы с базой данных:", e)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()









# import psycopg2
#
# try:
#     connection = psycopg2.connect(
#         database="postgres",
#         host="localhost",
#         user="postgres",
#         password="admin", port="5432"
#     )
#
#     cursor = connection.cursor()
# except:
#     print("error")
#
# # cursor.execute("DROP TABLE users_12345")
# query: str = """
#     CREATE TABLE IF NOT EXISTS users_12345 (
#         id serial PRIMARY KEY,
#         login varchar(32) NOT NULL,
#         password varchar(32) NOT NULL,
#         balance DECIMAL
#     );
# """
#
# cursor.execute(query=query)
# connection.commit()
#
# # Простой пример транзакции с конструкцией BEGIN; COMMIT; - начало; конец; Транзакции
# query2: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('first_user', '12345', 0.0);
#
#     COMMIT;
#
#
# """
#
# cursor.execute(query=query2)
#
# # Делаем несколько действий в одной транзакции пользователя
# query3: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('second_user', '0123456789', 0.0);
#
#     UPDATE users_12345 SET balance = balance + 1000
#     WHERE login='second_user';
#
#     UPDATE users_12345 SET balance = balance + 500
#     WHERE login='first_user';
#
#     UPDATE users_12345 SET balance = balance - 500
#     WHERE login='second_user';
#
#     COMMIT;
#
#
# """
#
# # cursor.execute(query=query3)
#
#
# # Откатываем все изменения во всей транзакции полностью
# query4: str = """
#     BEGIN;
#
#     UPDATE users_12345 SET login = 'changed_login'
#     WHERE login='first_user';
#
#     ROLLBACK;
# """
# cursor.execute(query=query4)
#
# # Откатываем часть изменений в транзакции до определнного "SAVEPOINT'а"
# query5: str = """
#     BEGIN;
#
#     UPDATE users_12345 SET password = 'super_new_password'
#     WHERE login='second_user';
#
#     SAVEPOINT change_password;
#
#     UPDATE users_12345 SET balance = balance - 500
#     WHERE login='first_user';
#
#     UPDATE users_12345 SET balance = balance + 500
#     WHERE login='second_user';
#
#     ROLLBACK TO SAVEPOINT change_password;
#
#
#     COMMIT;
# """
# cursor.execute(query=query5)
#
# get_users_query: str = """
#     SELECT * FROM users_12345;
# """
# cursor.execute(query=get_users_query)
#
# data: list[tuple] = cursor.fetchall()
# print(data)























# import psycopg2
#
# try:
#     connection = psycopg2.connect(
#         database="postgres",
#         host="localhost",
#         user="postgres",
#         password="admin", port="5432"
#     )
#
#     cursor = connection.cursor()
# except:
#     print("error")
#
# # cursor.execute("DROP TABLE users_12345")
# query: str = """
#     CREATE TABLE IF NOT EXISTS users_12345 (
#         id serial PRIMARY KEY,
#         login varchar(32) NOT NULL,
#         password varchar(32) NOT NULL,
#         balance DECIMAL
#     );
# """
#
# cursor.execute(query=query)
# connection.commit()
#
# # Простой пример транзакции с конструкцией BEGIN; COMMIT; - начало; конец; Транзакции
# query2: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('first_user', '12345', 0.0);
#
#     COMMIT;
#
#
# """
#
# cursor.execute(query=query2)
#
# # Делаем несколько действий в одной транзакции пользователя
# query3: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('second_user', '0123456789', 0.0);
#
#     UPDATE users_12345 SET balance = balance + 1000
#     WHERE login='second_user';
#
#     UPDATE users_12345 SET balance = balance + 500
#     WHERE login='first_user';
#
#     UPDATE users_12345 SET balance = balance - 500
#     WHERE login='second_user';
#
#     COMMIT;
#
#
# """
#
# # cursor.execute(query=query3)
#
#
# # Откатываем все изменения во всей транзакции полностью
# query4: str = """
#     BEGIN;
#
#     UPDATE users_12345 SET login = 'changed_login'
#     WHERE login='first_user';
#
#     ROLLBACK;
# """
# cursor.execute(query=query4)
#
# # Откатываем часть изменений в транзакции до определнного "SAVEPOINT'а"
# query5: str = """
#     BEGIN;
#
#     UPDATE users_12345 SET password = 'super_new_password'
#     WHERE login='second_user';
#
#     SAVEPOINT change_password;
#
#     UPDATE users_12345 SET balance = balance - 500
#     WHERE login='first_user';
#
#     UPDATE users_12345 SET balance = balance + 500
#     WHERE login='second_user';
#
#     ROLLBACK TO SAVEPOINT change_password;
#
#
#     COMMIT;
# """
# cursor.execute(query=query5)
#
# get_users_query: str = """
#     SELECT * FROM users_12345;
# """
# cursor.execute(query=get_users_query)
#
# data: list[tuple] = cursor.fetchall()
# print(data)












# import psycopg2
#
# try:
#     # Подключение к базе данных
#     connection = psycopg2.connect(
#         database="postgres",
#         host="localhost",
#         user="postgres",
#         password="admin",
#         port="5432"
#     )
#
#     cursor = connection.cursor()
#
#     # Создание таблицы, если она не существует
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS users_12345 (
#             id SERIAL PRIMARY KEY,
#             login VARCHAR(32) NOT NULL,
#             password VARCHAR(32) NOT NULL,
#             balance DECIMAL
#         );
#     """
#     cursor.execute(create_table_query)
#     connection.commit()
#
#     # Начало транзакции
#     connection.autocommit = False
#     cursor.execute("BEGIN;")
#
#     # Добавление пользователей
#     cursor.execute("INSERT INTO users_12345 (login, password, balance) VALUES ('first_user', '12345', 0.0);")
#     cursor.execute("INSERT INTO users_12345 (login, password, balance) VALUES ('second_user', '0123456789', 0.0);")
#
#     # Обновление баланса пользователей
#     cursor.execute("UPDATE users_12345 SET balance = balance + 1000 WHERE login='second_user';")
#     cursor.execute("UPDATE users_12345 SET balance = balance + 500 WHERE login='first_user';")
#     cursor.execute("UPDATE users_12345 SET balance = balance - 500 WHERE login='second_user';")
#
#     # Изменение логина и откат изменений
#     cursor.execute("UPDATE users_12345 SET login = 'changed_login' WHERE login='first_user';")
#     cursor.execute("ROLLBACK;")
#
#     # Получение данных пользователей
#     get_users_query = "SELECT * FROM users_12345;"
#     cursor.execute(get_users_query)
#     data = cursor.fetchall()
#     print(data)
#
#     # Конец транзакции
#     connection.commit()
#     connection.autocommit = True
# except psycopg2.Error as e:
#     connection.rollback()
#     print("Ошибка работы с базой данных:", e)
# finally:
#     # Закрытие соединения с базой данных
#     if connection:
#         cursor.close()
#         connection.close()
#



















# import psycopg2
#
# try:
#     connection = psycopg2.connect(
#         database="postgres",
#         host="localhost",
#         user="postgres",
#         password="admin", port="5432"
#     )
#
#     cursor = connection.cursor()
# except:
#     print("error")
#
# # cursor.execute("DROP TABLE users_12345")
# query: str = """
#     CREATE TABLE IF NOT EXISTS users_12345 (
#         id serial PRIMARY KEY,
#         login varchar(32) NOT NULL,
#         password varchar(32) NOT NULL,
#         balance DECIMAL
#     );
# """
#
# cursor.execute(query=query)
# connection.commit()
#
# query2: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('first_user', '12345', 0.0);
#
#     COMMIT;
#
#
# """
#
# cursor.execute(query=query2)
#
# query3: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('second_user', '0123456789', 0.0);
#
#     UPDATE users_12345 SET balance = balance + 1000
#     WHERE login='second_user';
#
#     UPDATE users_12345 SET balance = balance + 500
#     WHERE login='first_user';
#
#     UPDATE users_12345 SET balance = balance - 500
#     WHERE login='second_user';
#
#     COMMIT;
#
#
# """
#
# # cursor.execute(query=query3)
#
#
# query4: str = """
#     BEGIN;
#
#     UPDATE users_12345 SET login = 'changed_login'
#     WHERE login='first_user';
#
#     ROLLBACK;
# """
# cursor.execute(query=query4)
#
# query5: str = """
#     BEGIN;
#
#     UPDATE users_12345 SET password = 'super_new_password'
#     WHERE login='second_user';
#
#     SAVEPOINT change_password;
#
#     UPDATE users_12345 SET balance = balance - 500
#     WHERE login='first_user';
#
#     UPDATE users_12345 SET balance = balance + 500
#     WHERE login='second_user';
#
#     ROLLBACK TO SAVEPOINT change_password;
#
#
#     COMMIT;
# """
# cursor.execute(query=query5)
#
# get_users_query: str = """
#     SELECT * FROM users_12345;
# """
# cursor.execute(query=get_users_query)
# data: list[tuple] = cursor.fetchall()
# print(data)



































# import psycopg2
#
# try:
#     connection = psycopg2.connect(
#         database="postgres",
#         host="localhost",
#         user="postgres",
#         password="admin", port="5432"
#     )
#
#     cursor = connection.cursor()
# except:
#     print("error")
#
# # cursor.execute("DROP TABLE users_12345")
# query: str = """
#     CREATE TABLE IF NOT EXISTS users_12345 (
#         id serial PRIMARY KEY,
#         login varchar(32) NOT NULL,
#         password varchar(32) NOT NULL,
#         balance DECIMAL
#     );
# """
#
# cursor.execute(query=query)
# connection.commit()
#
# query2: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('first_user', '12345', 0.0);
#
#     COMMIT;
#
#
# """
#
# cursor.execute(query=query2)
#
# query3: str = """
#     BEGIN;
#
#     INSERT INTO users_12345
#     (login, password, balance)
#     VALUES ('second_user', '0123456789', 0.0);
#
#     UPDATE users_12345 SET balance = balance + 1000
#     WHERE login='second_user';
#
#     UPDATE users_12345 SET balance = balance + 500
#     WHERE login='first_user';
#
#     UPDATE users_12345 SET balance = balance - 500
#     WHERE login='second_user';
#
#     COMMIT;
#
#
# """
#
# cursor.execute(query=query3)
#
# query4: str = """
#     BEGIN;
#
#     UPDATE users_12345 SET login = 'changed_login'
#     WHERE login='first_user';
#
#     ROLLBACK;
# """
# cursor.execute(query=query4)
#
# get_users_query: str = """
#     SELECT * FROM users_12345;
# """
# cursor.execute(query=get_users_query)
# data: list[tuple] = cursor.fetchall()
# print(data)








# import psycopg2
# import secrets
# import string
#
# def generate_random_password(length=20):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(characters) for _ in range(length))
#
# # Функция для авторизации пользователя
# def authorize_user(connect):
#     attempts = 3
#     while attempts > 0:
#         user_name = input("Введите логин: ")
#         user_password = input("Введите пароль: ")
#
#         with connect.cursor() as cur:
#             cur.execute(
#                 """
#                 SELECT user_id FROM users WHERE user_name = %s AND user_password = %s
#                 """, (user_name, user_password)
#             )
#             user = cur.fetchone()
#
#             if user:
#                 print("Авторизация успешна.")
#                 return True
#             else:
#                 print("Неправильный логин или пароль.")
#                 attempts -= 1
#                 print(f"Осталось попыток: {attempts}")
#
#         if attempts == 0:
#             print("Превышено количество попыток.")
#             return False
#
# # Функция для регистрации нового пользователя
# def register_user(connect):
#     user_name = input("Введите логин: ")
#     user_password = input("Введите пароль: ")
#
#     with connect.cursor() as cur:
#         cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{user_name}\';')
#         user = cur.fetchone()
#
#         if user:
#             print("Данный никнейм уже занят!")
#         elif len(user_password) < 8:
#             print("Ваш пароль не может содержать меньше 8 символов!")
#         else:
#             cur.execute(
#                 """
#                 INSERT INTO users (user_name, user_password) VALUES
#                 (%s, %s)
#                 """, (user_name, user_password)
#             )
#             connect.commit()
#             print("Пользователь успешно зарегистрирован.")
#
# # Функция для создания суперпользователя
# def create_super_user(connect):
#     super_user_name = "super_user"
#     super_user_password = generate_random_password()
#
#     with connect.cursor() as cur:
#         cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{super_user_name}\';')
#         user = cur.fetchone()
#
#         if user:
#             print("Суперпользователь уже существует.")
#         else:
#             cur.execute(
#                 """
#                 INSERT INTO users (user_name, user_password, user_role) VALUES
#                 (%s, %s, %s)
#                 """, (super_user_name, super_user_password, "admin")
#             )
#             connect.commit()
#             print("Суперпользователь успешно создан.")
#             print("Ваш пароль:", super_user_password)
#
# # Подключение к базе данных
# with psycopg2.connect(
#         dbname="work_db",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
# ) as connect:
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS users
#             (
#                 user_id serial PRIMARY KEY,
#                 user_name VARCHAR(100) UNIQUE NOT NULL,
#                 user_password VARCHAR(100),
#                 user_role VARCHAR(100) DEFAULT 'guest',
#                 CONSTRAINT user_role_good CHECK (user_role IN ('admin', 'user', 'guest')),
#                 CONSTRAINT pass_len_chek CHECK (LENGTH(user_password) >= 8)
#             )
#             """
#         )
#         connect.commit()
#
#     # Выбор между авторизацией и регистрацией
#     actions = {
#         '1': authorize_user,
#         '2': register_user,
#     }
#
#     action = input("Выберите действие: 1 - Авторизация, 2 - Регистрация: ")
#
#     if action in actions:
#         actions[action](connect)
#     else:
#         print("Неправильный выбор действия.")
#
#     # Создание суперпользователя
#     create_super_user(connect)














# import psycopg2
# import secrets
# import string
#
# def generate_random_password(length=20):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(characters) for _ in range(length))
#
# # Функция для авторизации пользователя
# def authorize_user(connect):
#     attempts = 3
#     while attempts > 0:
#         user_name = input("Введите логин: ")
#         user_password = input("Введите пароль: ")
#
#         with connect.cursor() as cur:
#             cur.execute(
#                 """
#                 SELECT user_id FROM users WHERE user_name = %s AND user_password = %s
#                 """, (user_name, user_password)
#             )
#             user = cur.fetchone()
#
#             if user:
#                 print("Авторизация успешна.")
#                 return True
#             else:
#                 print("Неправильный логин или пароль.")
#                 attempts -= 1
#                 print(f"Осталось попыток: {attempts}")
#
#         if attempts == 0:
#             print("Превышено количество попыток.")
#             return False
#
# # Функция для регистрации нового пользователя
# def register_user(connect):
#     user_name = input("Введите логин: ")
#     user_password = input("Введите пароль: ")
#
#     with connect.cursor() as cur:
#         cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{user_name}\';')
#         user = cur.fetchone()
#
#         if user:
#             print("Данный никнейм уже занят!")
#         elif len(user_password) < 8:
#             print("Ваш пароль не может содержать меньше 8 символов!")
#         else:
#             cur.execute(
#                 """
#                 INSERT INTO users (user_name, user_password) VALUES
#                 (%s, %s)
#                 """, (user_name, user_password)
#             )
#             connect.commit()
#             print("Пользователь успешно зарегистрирован.")
#
# # Подключение к базе данных
# with psycopg2.connect(
#         dbname="work_db",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
# ) as connect:
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS users
#             (
#                 user_id serial PRIMARY KEY,
#                 user_name VARCHAR(100) UNIQUE NOT NULL,
#                 user_password VARCHAR(100),
#                 user_role VARCHAR(100) DEFAULT 'guest',
#                 CONSTRAINT user_role_good CHECK (user_role IN ('admin', 'user', 'guest')),
#                 CONSTRAINT pass_len_chek CHECK (LENGTH(user_password) >= 8)
#             )
#             """
#         )
#         connect.commit()
#
#     # Выбор между авторизацией и регистрацией
#     actions = {
#         '1': authorize_user,
#         '2': register_user,
#     }
#
#     action = input("Выберите действие: 1 - Авторизация, 2 - Регистрация: ")
#
#     if action in actions:
#         actions[action](connect)
#     else:
#         print("Неправильный выбор действия.")









# import psycopg2
# import secrets
# import string
#
# def generate_random_password(length=20):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(characters) for _ in range(length))
#
# # Подключение к базе данных
# with psycopg2.connect(
#         dbname="work_db",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
# ) as connect:
#     # Для создания таблицы
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS users
#             (
#                 user_id serial PRIMARY KEY,
#                 user_name VARCHAR(100) UNIQUE NOT NULL,
#                 user_password VARCHAR(100),
#                 user_role VARCHAR(100) DEFAULT 'guest',
#                 CONSTRAINT user_role_good CHECK (user_role IN ('admin', 'user', 'guest')),
#                 CONSTRAINT pass_len_chek CHECK (LENGTH(user_password) >= 8)
#             )
#             """
#         )
#         connect.commit()
#
#     # Выбор между авторизацией и регистрацией
#     action = input("Выберите действие: 1 - Авторизация, 2 - Регистрация: ")
#
#     if action == '1':  # Авторизация
#         attempts = 3
#         while attempts > 0:
#             with connect.cursor() as cur:
#                 user_name = input("Введите логин: ")
#                 user_password = input("Введите пароль: ")
#
#                 # Проверка наличия пользователя с указанным логином и паролем
#                 cur.execute(
#                     """
#                     SELECT user_id FROM users WHERE user_name = %s AND user_password = %s
#                     """, (user_name, user_password)
#                 )
#                 user = cur.fetchone()
#
#                 if user:
#                     print("Авторизация успешна.")
#                     break
#                 else:
#                     print("Неправильный логин или пароль.")
#                     attempts -= 1
#                     print(f"Осталось попыток: {attempts}")
#
#             if attempts == 0:
#                 print("Превышено количество попыток.")
#     elif action == '2':  # Регистрация
#         with connect.cursor() as cur:
#             user_name = input("Введите логин: ")
#             user_password = input("Введите пароль: ")
#
#             # Проверка наличия пользователя с таким логином
#             cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{user_name}\';')
#             user = cur.fetchone()
#
#             if user:
#                 print("Данный никнейм уже занят!")
#             elif len(user_password) < 8:
#                 print("Ваш пароль не может содержать меньше 8 символов!")
#             else:
#                 # Ввод нового пользователя и его пароля
#                 cur.execute(
#                     """
#                     INSERT INTO users (user_name, user_password) VALUES
#                     (%s, %s)
#                     """, (user_name, user_password)
#                 )
#                 connect.commit()
#                 print("Пользователь успешно зарегистрирован.")
#     else:
#         print("Неправильный выбор действия.")



# import psycopg2
# import secrets
# import string
#
# def generate_random_password(length=20):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(characters) for _ in range(length))
#
# # Подключение к базе данных
# with psycopg2.connect(
#         dbname="work_db",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
# ) as connect:
#     # Для создания таблицы
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS users
#             (
#                 user_id serial PRIMARY KEY,
#                 user_name VARCHAR(100) UNIQUE NOT NULL,
#                 user_password VARCHAR(100),
#                 user_role VARCHAR(100) DEFAULT 'user',
#                 CONSTRAINT user_role_good CHECK (user_role IN ('admin', 'user')),
#                 CONSTRAINT pass_len_chek CHECK (LENGTH(user_password) >= 8)
#             )
#             """
#         )
#         connect.commit()
#
#     # Регистрация
#     with connect.cursor() as cur:
#         user_name = input("Введите логин: ")
#         user_password = input("Введите пароль: ")
#
#         # Проверка наличия пользователя с таким логином
#         cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{user_name}\';')
#         user = cur.fetchone()
#
#         if user:
#             print("Данный никнейм уже занят!")
#         elif len(user_password) < 8:
#             print("Ваш пароль не может содержать меньше 8 символов!")
#         else:
#             # Ввод нового пользователя и его пароля
#             cur.execute(
#                 """
#                 INSERT INTO users (user_name, user_password) VALUES
#                 (%s, %s)
#                 """, (user_name, user_password)
#             )
#             connect.commit()
#             print("Пользователь успешно зарегистрирован.")
#
#     # Авторизация
#     attempts = 3
#     while attempts > 0:
#         with connect.cursor() as cur:
#             user_name = input("Введите логин: ")
#             user_password = input("Введите пароль: ")
#
#             # Проверка наличия пользователя с указанным логином и паролем
#             cur.execute(
#                 """
#                 SELECT user_id FROM users WHERE user_name = %s AND user_password = %s
#                 """, (user_name, user_password)
#             )
#             user = cur.fetchone()
#
#             if user:
#                 print("Авторизация успешна.")
#                 break
#             else:
#                 print("Неправильный логин или пароль.")
#                 attempts -= 1
#                 print(f"Осталось попыток: {attempts}")
#
#         if attempts == 0:
#             print("Превышено количество попыток.")





# import psycopg2
#
# with psycopg2.connect(
#         dbname="work_db",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432",
# ) as connect:
#     # Для создания таблицы
#     with connect.cursor() as cur:
#         cur.execute(
#             """
#         CREATE TABLE IF NOT EXISTS users
#         (
#             user_id serial,
#             user_name VARCHAR(100),
#             user_password VARCHAR(100),
#             user_role VARCHAR(100) DEFAULT 'user',
#
#             CONSTRAINT pk_user_id PRIMARY KEY (user_id),
#             CONSTRAINT unique_user_name UNIQUE (user_name),
#             CONSTRAINT user_role_good CHECK (user_role IN ('admin', 'user')) ,
#             CONSTRAINT pass_len_chek CHECK (LENGTH(user_password) >= 8)
#         )
#         """)
#         connect.commit()
#
#     # Регистрация correct
#     with connect.cursor() as cur:
#         user_name = input("Введите логин: ")
#         user_password = input("Введите пароль: ")
#
#         cur.execute(f'SELECT user_id FROM users WHERE user_name = \'{user_name}\';')
#
#         user = cur.fetchone()
#
#         if user:
#             print("Данный никнейм уже занят!")
#         elif len(user_password) < 8:
#             print("Ваш пароль не может содержать меньше 8 символов!")
#         else:
#             cur.execute(
#                 f"""
#                 INSERT INTO users (user_name, user_password) VALUES
#                 ('{user_name}', '{user_password}')
#                 """
#             )
#             connect.commit()

# import psycopg2
#
#
# connect =  psycopg2.connect(
#     dbname="postgres",
#     user="postgres",
#     password="admin",
#     host="localhost",
#     port="5432",
# )
# connect.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
# cur =  connect.cursor()
# cur.execute(
#         """
# CREATE DATABASE work_db;
# """)

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
#     with connect.cursor() as cur:
#         # Создать таблицу пользователей, если она не существует
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
#
#         # Создать таблицу продуктов, если она не существует
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
#
#         connect.commit()
#
#     # Добавить пользователя и его товары
#     with connect.cursor() as cur:
#         user_name = input("Введите логин: ")
#         user_password = input("Введите пароль: ")
#         hashed_password = hash_password(user_password)
#         products_data = [
#             ("Молоко", 2),
#             ("Хлеб", 1),
#             ("Яйца", 6),
#             ("Масло", 1),
#             ("Сыр", 2)
#         ]
#         try:
#             cur.execute(
#                 """
#                 INSERT INTO users (username, password)
#                 VALUES (%s, %s)
#                 RETURNING user_id
#                 """, (user_name, hashed_password)
#             )
#             user_id = cur.fetchone()[0]
#             cur.executemany(
#                 """
#                 INSERT INTO products (user_id, name, quantity)
#                 VALUES (%s, %s, %s)
#                 """, [(user_id, name, quantity) for name, quantity in products_data]
#             )
#             connect.commit()
#         except psycopg2.errors.UniqueViolation as error:
#             print("Пользователь с таким никнеймом уже существует!")
#             connect.rollback()
#
#     # Получить пользователя и его товары
#     with connect.cursor() as cur:
#         login = input("Введите ваш логин: ")
#         password = input("Введите ваш пароль: ")
#         hashed_password = hash_password(password)
#         cur.execute(
#             """
#             SELECT u.username, p.name, p.quantity
#             FROM users u
#             JOIN products p ON u.user_id = p.user_id
#             WHERE u.username = %s AND u.password = %s
#             """, (login, hashed_password)
#         )
#         user_products = cur.fetchall()
#
#         if not user_products:
#             print("Не верные данные!")
#         else:
#             print("Вы вошли в систему!")
#             total_quantity = sum(product[2] for product in user_products)
#             print("Товары пользователя:")
#             for product in user_products:
#                 print(f"Название: {product[1]}, Количество: {product[2]}")
#             print(f"Общее количество купленных товаров: {total_quantity}")
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