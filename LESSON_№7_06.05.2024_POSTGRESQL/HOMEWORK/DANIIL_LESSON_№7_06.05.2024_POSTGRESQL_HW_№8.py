# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 06 - 07 МАЯ 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                              ДОМАШНЯЯ РАБОТА

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                            Дисциплина: Теория баз данных. PostgreSQL

                                            Понятие транзакции.
                                            Домашняя работа №8:
                    (предполагаю, что тема будет такая же, как и в Практической Работе №8)
                             Понятие представления. Материализованное представление.

                                        👇🏻 Выполните следующие задания:

👉🏻 Задание № 1.
Создайте представление которое будет выводить список сотрудников, отсортированный по возрастанию зарплаты.

👉🏻 Задание № 2.
Создайте запрос, который объединяет две таблицы - "пользователи" и "посты", и
выводит список всех пользователей и количество их постов.


👉🏻 Задание № 3.
Создайте материализованное представление, 
которое будет выводить суммарное количество заказов и общую сумму по каждому месяцу за последний год.

👉🏻 Обязательно:
Максимально там где нужно добавлять, вставлять, обновлять данные.
👉🏻 (Используйте Транзакции)!!!!!
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 06.05.2024 - учитель Хуснуллин Даниил Денисович.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
from faker import Faker
import psycopg2
import random
from datetime import datetime, timedelta


# Подключение к серверу PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="admin",
    port="5432"
)

# Создание базы данных
def create_database():
    try:
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        create_database_query = "CREATE DATABASE my_hw_ls_71_db"
        cursor.execute(create_database_query)
        print("База данных my_hw_ls_71_db успешно создана.")
    except psycopg2.Error as e:
        print("Ошибка при создании базы данных my_hw_ls_71_db:", e)
    finally:
        if connection:
            cursor.close()

# Вызываем функцию для создания базы данных
create_database()

# Подключение к созданной базе данных
connection = psycopg2.connect(
    database="my_hw_ls_71_db",
    host="localhost",
    user="postgres",
    password="admin",
    port="5432"
)

# Создание таблицы Employees
def create_employees_table():
    try:
        cursor = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Employees (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                birth_date DATE,
                position VARCHAR(50),
                gender VARCHAR(10),
                marital_status VARCHAR(20),
                children BOOLEAN,
                country VARCHAR(50),
                city VARCHAR(50),
                salary NUMERIC
            );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица Employees успешно создана.")
        # Заполнение таблицы данными
        fake = Faker()
        for _ in range(10):  # Генерируем 10 случайных сотрудников
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
            position = fake.job()
            gender = random.choice(["Male", "Female"])
            marital_status = random.choice(["Single", "Married"])
            children = random.choice([True, False])
            country = fake.country()
            city = fake.city()
            salary = round(random.uniform(1000, 5000), 2)  # Генерация случайной зарплаты
            insert_query = """
                INSERT INTO Employees (first_name, last_name, birth_date, position, gender, marital_status, children, country, city, salary)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (first_name, last_name, birth_date, position, gender, marital_status, children, country, city, salary))
        connection.commit()
        print("Данные успешно добавлены в таблицу Employees.")
    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()

# Вызываем функцию для создания таблицы сотрудников и заполнения её данными
create_employees_table()

# Создание таблицы Posts
def create_posts_table():
    try:
        cursor = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Posts (
                id SERIAL PRIMARY KEY,
                employee_id INT REFERENCES Employees(id),
                post_count INT
            );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица Posts успешно создана.")
        # Заполнение таблицы данными
        for employee_id in range(1, 11):  # Проходим по каждому сотруднику
            post_count = random.randint(1, 10)  # Генерация случайного количества постов
            insert_query = """
                INSERT INTO Posts (employee_id, post_count)
                VALUES (%s, %s);
            """
            cursor.execute(insert_query, (employee_id, post_count))
        connection.commit()
        print("Данные успешно добавлены в таблицу Posts.")
    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()

# Создание таблицы Orders
def create_orders_table():
    try:
        cursor = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Orders (
                id SERIAL PRIMARY KEY,
                employee_id INT REFERENCES Employees(id),
                order_count INT,
                order_date DATE
            );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица Orders успешно создана.")
        # Заполнение таблицы данными
        fake = Faker()
        for employee_id in range(1, 11):  # Проходим по каждому сотруднику
            order_count = random.randint(1, 5)  # Генерация случайного количества заказов
            order_date = fake.date_time_between(start_date='-1y', end_date='now').date()  # Генерация случайной даты
            insert_query = """
                INSERT INTO Orders (employee_id, order_count, order_date)
                VALUES (%s, %s, %s);
            """
            cursor.execute(insert_query, (employee_id, order_count, order_date))
        connection.commit()
        print("Данные успешно добавлены в таблицу Orders.")
    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()


# Вызываем функции для создания таблиц для постов и заказов и заполнения их данными
create_posts_table()
create_orders_table()

# Создание представления для списка сотрудников, отсортированного по возрастанию зарплаты
def create_sorted_employees_view():
    try:
        cursor = connection.cursor()
        create_view_query = """
            CREATE OR REPLACE VIEW SortedEmployees AS
            SELECT * FROM Employees
            ORDER BY salary;
        """
        cursor.execute(create_view_query)
        connection.commit()
        print("Представление SortedEmployees успешно создано.")
    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()

# Вызываем функцию для создания представления
create_sorted_employees_view()

# Создание запроса для объединения двух таблиц и вывода списка всех пользователей и количества их постов
def get_users_posts():
    try:
        cursor = connection.cursor()
        get_users_posts_query = """
            SELECT e.id, e.first_name, e.last_name, COALESCE(p.post_count, 0) AS post_count
            FROM Employees e
            LEFT JOIN Posts p ON e.id = p.employee_id
            ORDER BY e.id;
        """
        cursor.execute(get_users_posts_query)
        users_posts = cursor.fetchall()
        print("\nСписок пользователей и количество их постов:")
        for user_post in users_posts:
            print(user_post)
    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()

# Вызываем функцию для получения списка пользователей и количества их постов
get_users_posts()

# Создание материализованного представления для подсчета суммарного количества заказов и общей суммы по каждому месяцу за последний год
def create_orders_summary_materialized_view():
    try:
        cursor = connection.cursor()

        create_materialized_view_query = """
            CREATE MATERIALIZED VIEW OrdersSummary AS
            SELECT
                DATE_TRUNC('month', order_date) AS month,
                COUNT(id) AS order_count,
                SUM(order_count) AS total_count
            FROM Orders
            WHERE EXTRACT(YEAR FROM order_date) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY DATE_TRUNC('month', order_date);
        """
        cursor.execute(create_materialized_view_query)
        connection.commit()

        print("Материализованное представление OrdersSummary успешно создано.")

    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()


# Вызываем функцию для создания материализованного представления
create_orders_summary_materialized_view()

# Закрытие соединения с базой данных
if connection:
    connection.close()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг за шагом. Разбор кода, для Вас и для меня самого в будущем. Ведь я сейчас, не я через пол года.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 1:
# Создание базы данных
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Создание базы данных.

# Описание: В этом шаге создается база данных PostgreSQL с именем "my_hw_ls_71_db".

# Пример кода:

# Подключение к серверу PostgreSQL
# connection = psycopg2.connect(
#     host="localhost",
#     user="postgres",
#     password="admin",
#     port="5432"
# )

# Создание базы данных

# def create_database():
#     try:
#         connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
#         cursor = connection.cursor()
#         create_database_query = "CREATE DATABASE my_hw_ls_71_db"
#         cursor.execute(create_database_query)
#         print("База данных my_hw_ls_71_db успешно создана.")
#     except psycopg2.Error as e:
#         print("Ошибка при создании базы данных my_hw_ls_71_db:", e)
#     finally:
#         if connection:
#             cursor.close()
#
# Вызываем функцию для создания базы данных
# create_database()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода устанавливается соединение с сервером PostgreSQL с использованием учетных данных
# (хост, имя пользователя, пароль и порт). Затем создается функция create_database(), которая отвечает за создание
# базы данных с именем "my_hw_ls_71_db". Функция выполняет запрос на создание базы данных, а затем выводит сообщение
# об успешном создании или сообщение об ошибке при возникновении исключения. В конце блока вызывается
# функция create_database(), чтобы создать базу данных.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 2:
# Создание таблицы Employees и заполнение её данными
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Создание таблицы Employees.

# Описание:
# В этом шаге создается таблица "Employees" в базе данных "my_hw_ls_71_db".
# Таблица содержит информацию о сотрудниках, такую как их идентификатор, имя, фамилия, дата рождения,
# должность, пол, семейное положение, наличие детей, страна, город и зарплата. После создания таблицы она заполняется
# данными о 10 случайных сотрудниках с использованием библиотеки Faker для генерации случайных данных.

# Пример кода:

# Подключение к созданной базе данных

# connection = psycopg2.connect(
#     database="my_hw_ls_71_db",
#     host="localhost",
#     user="postgres",
#     password="admin",
#     port="5432"
# )

# Создание таблицы Employees

# def create_employees_table():
#     try:
#         cursor = connection.cursor()
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS Employees (
#                 id SERIAL PRIMARY KEY,
#                 first_name VARCHAR(50),
#                 last_name VARCHAR(50),
#                 birth_date DATE,
#                 position VARCHAR(50),
#                 gender VARCHAR(10),
#                 marital_status VARCHAR(20),
#                 children BOOLEAN,
#                 country VARCHAR(50),
#                 city VARCHAR(50),
#                 salary NUMERIC
#             );
#         """
#         cursor.execute(create_table_query)
#         connection.commit()
#         print("Таблица Employees успешно создана.")
#         # Заполнение таблицы данными
#         fake = Faker()
#         for _ in range(10):  # Генерируем 10 случайных сотрудников
#             first_name = fake.first_name()
#             last_name = fake.last_name()
#             birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
#             position = fake.job()
#             gender = random.choice(["Male", "Female"])
#             marital_status = random.choice(["Single", "Married"])
#             children = random.choice([True, False])
#             country = fake.country()
#             city = fake.city()
#             salary = round(random.uniform(1000, 5000), 2)  # Генерация случайной зарплаты
#             insert_query = """
#                 INSERT INTO Employees (first_name, last_name, birth_date, position, gender, marital_status, children, country, city, salary)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
#             """
#             cursor.execute(insert_query, (first_name, last_name, birth_date, position, gender, marital_status, children, country, city, salary))
#         connection.commit()
#         print("Данные успешно добавлены в таблицу Employees.")
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()
#
# Вызываем функцию для создания таблицы сотрудников и заполнения её данными
# create_employees_table()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода сначала устанавливается соединение с созданной базой данных "my_hw_ls_71_db".
# Затем создается функция create_employees_table(), которая отвечает за создание таблицы "Employees".
# Структура таблицы включает в себя столбцы для идентификатора, имени, фамилии, даты рождения, должности, пола,
# семейного положения, наличия детей, страны, города и зарплаты сотрудников.
# После создания таблицы она заполняется данными о 10 случайных сотрудниках с использованием библиотеки Faker
# для генерации случайных данных. Каждый сотрудник добавляется в таблицу с помощью SQL-запроса INSERT INTO,
# используя сгенерированные случайные данные. В конце блока вызывается функция create_employees_table(),
# чтобы создать таблицу и заполнить её данными.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 3:
# Создание таблицы Posts и заполнение её данными
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Создание таблицы Posts.

# Описание:
# В этом шаге создается таблица "Posts" в базе данных "my_hw_ls_71_db".
# Таблица содержит информацию о постах сотрудников, включая идентификатор поста,
# идентификатор сотрудника (внешний ключ), количество постов. После создания таблицы она заполняется данными
# о количестве постов для каждого сотрудника. Количество постов генерируется случайным образом для каждого
# сотрудника в диапазоне от 1 до 10.

# Пример кода:

# Создание таблицы Posts

# def create_posts_table():
#     try:
#         cursor = connection.cursor()
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS Posts (
#                 id SERIAL PRIMARY KEY,
#                 employee_id INT REFERENCES Employees(id),
#                 post_count INT
#             );
#         """
#         cursor.execute(create_table_query)
#         connection.commit()
#         print("Таблица Posts успешно создана.")
#         # Заполнение таблицы данными
#         for employee_id in range(1, 11):  # Проходим по каждому сотруднику
#             post_count = random.randint(1, 10)  # Генерация случайного количества постов
#             insert_query = """
#                 INSERT INTO Posts (employee_id, post_count)
#                 VALUES (%s, %s);
#             """
#             cursor.execute(insert_query, (employee_id, post_count))
#         connection.commit()
#         print("Данные успешно добавлены в таблицу Posts.")
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()
#
# Вызываем функцию для создания таблицы для постов и заполнения её данными
# create_posts_table()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода создается функция create_posts_table(), которая отвечает за создание таблицы "Posts".
# Таблица содержит три столбца: идентификатор поста, идентификатор сотрудника
# (внешний ключ, связанный с таблицей "Employees") и количество постов. После создания таблицы она заполняется
# данными о количестве постов для каждого сотрудника. Для каждого сотрудника генерируется случайное количество
# постов в диапазоне от 1 до 10 с использованием функции random.randint(). Каждая запись в таблицу добавляется
# с помощью SQL-запроса INSERT INTO. В конце блока вызывается функция create_posts_table(), чтобы создать
# таблицу и заполнить её данными.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 4:
# Создание таблицы Orders и заполнение её данными
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Создание таблицы Orders.

# Описание:
# В этом шаге создается таблица "Orders" в базе данных "my_hw_ls_71_db".
# Таблица содержит информацию о заказах сотрудников, включая идентификатор заказа, идентификатор сотрудника
# (внешний ключ), количество заказов и дату заказа. После создания таблицы она заполняется данными о
# количестве заказов для каждого сотрудника. Количество заказов генерируется случайным образом для каждого
# сотрудника в диапазоне от 1 до 5, а дата заказа устанавливается как случайная дата за последний год.

# Пример кода:

# Создание таблицы Orders

# def create_orders_table():
#     try:
#         cursor = connection.cursor()
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS Orders (
#                 id SERIAL PRIMARY KEY,
#                 employee_id INT REFERENCES Employees(id),
#                 order_count INT,
#                 order_date DATE
#             );
#         """
#         cursor.execute(create_table_query)
#         connection.commit()
#         print("Таблица Orders успешно создана.")
#         # Заполнение таблицы данными
#         fake = Faker()
#         for employee_id in range(1, 11):  # Проходим по каждому сотруднику
#             order_count = random.randint(1, 5)  # Генерация случайного количества заказов
#             order_date = fake.date_time_between(start_date='-1y', end_date='now').date()  # Генерация случайной даты
#             insert_query = """
#                 INSERT INTO Orders (employee_id, order_count, order_date)
#                 VALUES (%s, %s, %s);
#             """
#             cursor.execute(insert_query, (employee_id, order_count, order_date))
#         connection.commit()
#         print("Данные успешно добавлены в таблицу Orders.")
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()
#
# # Вызываем функцию для создания таблицы заказов и заполнения её данными
# create_orders_table()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода создается функция create_orders_table(), которая отвечает за создание таблицы "Orders".
# Таблица содержит четыре столбца: идентификатор заказа, идентификатор сотрудника
# (внешний ключ, связанный с таблицей "Employees"), количество заказов и дату заказа.
# После создания таблицы она заполняется данными о количестве заказов для каждого сотрудника.
# Для каждого сотрудника генерируется случайное количество заказов в диапазоне от 1 до 5
# с использованием функции random.randint(). Для каждого заказа также генерируется случайная дата в пределах
# последнего года с помощью библиотеки Faker. Каждая запись в таблицу добавляется с помощью SQL-запроса INSERT INTO.
# В конце блока вызывается функция create_orders_table(), чтобы создать таблицу и заполнить её данными.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 5:
# Создание представления для списка сотрудников, отсортированного по возрастанию зарплаты
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Создание представления SortedEmployees.

# Описание:
# В этом шаге создается представление "SortedEmployees", которое содержит список сотрудников,
# отсортированных по возрастанию зарплаты. Данное представление позволяет получить упорядоченный список сотрудников
# в порядке возрастания их заработной платы.

# Пример кода:

# Создание представления для списка сотрудников, отсортированного по возрастанию зарплаты

# def create_sorted_employees_view():
#     try:
#         cursor = connection.cursor()
#         create_view_query = """
#             CREATE OR REPLACE VIEW SortedEmployees AS
#             SELECT * FROM Employees
#             ORDER BY salary;
#         """
#         cursor.execute(create_view_query)
#         connection.commit()
#         print("Представление SortedEmployees успешно создано.")
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()

# Вызываем функцию для создания представления
# create_sorted_employees_view()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода создается функция create_sorted_employees_view(),
# которая отвечает за создание представления "SortedEmployees".
# Представление формируется на основе таблицы "Employees" и содержит те же столбцы, что и таблица "Employees".
# Для формирования упорядоченного списка сотрудников представление сортируется по возрастанию
# зарплаты с помощью ключевого слова ORDER BY. В конце блока вызывается функция create_sorted_employees_view(),
# чтобы создать представление.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 6:
# Создание запроса для объединения двух таблиц и вывода списка всех пользователей и количества их постов
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Получение списка пользователей и количества их постов.

# Описание:
# В этом шаге создается запрос для объединения таблиц "Employees" и "Posts",
# чтобы получить список всех пользователей и количество их постов.
# Для этого используется операция объединения LEFT JOIN. Результаты запроса выводятся на экран.

# Пример кода:

# Создание запроса для объединения двух таблиц и вывода списка всех пользователей и количества их постов

# def get_users_posts():
#     try:
#         cursor = connection.cursor()
#         get_users_posts_query = """
#             SELECT e.id, e.first_name, e.last_name, COALESCE(p.post_count, 0) AS post_count
#             FROM Employees e
#             LEFT JOIN Posts p ON e.id = p.employee_id
#             ORDER BY e.id;
#         """
#         cursor.execute(get_users_posts_query)
#         users_posts = cursor.fetchall()
#         print("\nСписок пользователей и количество их постов:")
#         for user_post in users_posts:
#             print(user_post)
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()

# Вызываем функцию для получения списка пользователей и количества их постов
# get_users_posts()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода создается функция get_users_posts(), которая отвечает за получение списка пользователей
# и количества их постов. Для этого используется SQL-запрос, который объединяет таблицы "Employees" и "Posts" с
# помощью операции LEFT JOIN по полю "id". После выполнения запроса результаты выводятся на экран в
# формате "id пользователя, имя пользователя, фамилия пользователя, количество постов".
# Если у пользователя нет постов, используется функция COALESCE, чтобы заменить значение NULL на 0.
# В конце блока вызывается функция get_users_posts() для выполнения запроса.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 7:
# Создание материализованного представления для подсчета суммарного количества заказов и общей суммы
# по каждому месяцу за последний год
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Создание материализованного представления OrdersSummary.

# Описание:
# В этом шаге создается материализованное представление "OrdersSummary",
# которое используется для подсчета суммарного количества заказов и общей суммы по каждому месяцу за последний год.
# Для этого используется агрегирующая функция COUNT и SUM в сочетании с функцией GROUP BY,
# которая группирует данные по месяцам. Результаты запроса сохраняются в материализованное представление.

# Пример кода:

# Создание материализованного представления для подсчета суммарного количества заказов и общей
# суммы по каждому месяцу за последний год

# def create_orders_summary_materialized_view():
#     try:
#         cursor = connection.cursor()
#
#         create_materialized_view_query = """
#             CREATE MATERIALIZED VIEW OrdersSummary AS
#             SELECT
#                 DATE_TRUNC('month', order_date) AS month,
#                 COUNT(id) AS order_count,
#                 SUM(order_count) AS total_count
#             FROM Orders
#             WHERE EXTRACT(YEAR FROM order_date) = EXTRACT(YEAR FROM CURRENT_DATE)
#             GROUP BY DATE_TRUNC('month', order_date);
#         """
#         cursor.execute(create_materialized_view_query)
#         connection.commit()
#
#         print("Материализованное представление OrdersSummary успешно создано.")
#
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()
#
#
# Вызываем функцию для создания материализованного представления
# create_orders_summary_materialized_view()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода создается функция create_orders_summary_materialized_view(),
# которая отвечает за создание материализованного представления "OrdersSummary".
# В запросе используется агрегирующая функция COUNT, чтобы подсчитать количество заказов, и функция SUM,
# чтобы найти общее количество заказов за каждый месяц.
# Результаты группируются по месяцам с помощью функции DATE_TRUNC('month', order_date).
# Затем используется условие WHERE, чтобы выбрать заказы только за текущий год.
# После выполнения запроса результаты сохраняются в материализованное представление "OrdersSummary".
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг 8:
# Закрытие соединения с базой данных
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заголовок: Закрытие соединения с базой данных.

# Описание: В этом шаге происходит закрытие соединения с базой данных с помощью метода close().

# Пример кода:

# # Закрытие соединения с базой данных
# if connection:
#     connection.close()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Подробное описание:
# В этом блоке кода проверяется, существует ли соединение с базой данных. Если оно существует,
# то вызывается метод close(), который закрывает соединение с базой данных.
# Это важно для корректной работы и освобождения ресурсов после завершения работы с базой данных.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# СПАСИБО за внимание! Надеюсь, что Вы по достоинству оцените данную ДОМАШНЮЮ РАБОТУ №8 - от 06.05.2024-07.05.2024