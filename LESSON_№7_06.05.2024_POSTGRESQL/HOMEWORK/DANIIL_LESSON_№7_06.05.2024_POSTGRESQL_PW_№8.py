# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ПРАКТИЧЕСКОЙ РАБОТЫ: 06 - 07 МАЯ 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                              ПРАКТИЧЕСКАЯ РАБОТА

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                            Дисциплина: Теория баз данных. PostgreSQL

                                            Практическая работа №8:
                             Понятие представления. Материализованное представление.

                                        👇🏻 Выполните следующие задания:

👉🏻 Задание № 1.
Необходимо получить список игроков, их роль, гражданство, сумма минут, проведенных на поле и количество полученных
карточек за весь футбольный сезон.

👉🏻 Поля: 
- nickname, 
- role, 
- citizenship, 
- sum_minutes, 
- sum_cards

👉🏻 Отсортировать:
- голкипер, защитник, центральный полузащитник, нападающий;
- От большего к меньшему количеству минут на поле.


👉🏻 Задание № 2.
Создать одно простое представление, и одно материализованное представление.


👉🏻 Задание № 3.
Изменить количество минут у игрока «А.Becker» в игре №1 с 90 минут на 120 и посмотреть результат
в обоих представлениях.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 06.05.2024 - учитель Хуснуллин Даниил Денисович.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ДЛЯ НАЧАЛА - почему my_pw_ls_71_db?
# my - моя
# pw - практическая работа
# ls - урок №
# 7 - 7
# 1 - вариант 1
# db - база данных
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #



import psycopg2
from psycopg2 import sql

def create_database():
    try:
        # Подключение к серверу PostgreSQL
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="admin",
            port="5432"
        )

        # Отключение автоматического запуска транзакций
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()

        # Создание базы данных my_pw_ls_71_db, если она не существует
        create_database_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier("my_pw_ls_71_db"))
        cursor.execute(create_database_query)

        print("База данных my_pw_ls_71_db успешно создана.")

    except psycopg2.Error as e:
        print("Ошибка при создании базы данных my_pw_ls_71_db:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Вызываем функцию для создания базы данных
create_database()

def create_players_table():
    try:
        connection = psycopg2.connect(
            database="my_pw_ls_71_db",
            host="localhost",
            user="postgres",
            password="admin",
            port="5432"
        )

        cursor = connection.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS Players (
                id SERIAL PRIMARY KEY,
                nickname VARCHAR(50) NOT NULL,
                player_number INT NOT NULL,
                role VARCHAR(50) NOT NULL,
                citizenship VARCHAR(50) NOT NULL,
                sum_minutes INT NOT NULL,
                sum_cards INT NOT NULL
            );
        """
        cursor.execute(create_table_query)
        connection.commit()

        print("Таблица Players успешно создана.")

        # Добавим некоторые данные в таблицу
        insert_data_query = """
            INSERT INTO Players (nickname, player_number, role, citizenship, sum_minutes, sum_cards)
            VALUES
                ('Ivan_Ivan', 1, 'голкипер', 'Russia', 90, 2),
                ('Rio_Carnavele', 2, 'защитник', 'Brazil', 90, 1),
                ('Hitler_Kaput', 3, 'нападающий', 'Germany', 90, 1),
                ('Ole_Ole_Ole', 4, 'нападающий', 'Argentina', 90, 0),
                ('Zorro', 5, 'центральный полузащитник', 'Spain', 90, 2),
                ('Kruasan', 6, 'голкипер', 'France', 90, 1),
                ('Spagetti_Borgia', 7, 'защитник', 'Italy', 90, 2),
                ('Big_Ben_Booom', 8, 'центральный полузащитник', 'England', 90, 1),
                ('Ronaldo', 9, 'голкипер', 'Portugal', 90, 0),
                ('А.Becker', 10, 'нападающий', 'Netherlands', 90, 1);
        """
        cursor.execute(insert_data_query)
        connection.commit()

        print("Данные успешно добавлены в таблицу Players.")

    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Создаем таблицу и добавляем данные
create_players_table()

def task_1():
    try:
        connection = psycopg2.connect(
            database="my_pw_ls_71_db",
            host="localhost",
            user="postgres",
            password="admin",
            port="5432"
        )

        cursor = connection.cursor()

        # SQL-запрос для получения списка игроков с сортировкой
        get_players_query = """
            SELECT nickname, role, citizenship, sum_minutes, sum_cards
            FROM Players
            ORDER BY
                CASE role
                    WHEN 'голкипер' THEN 1
                    WHEN 'защитник' THEN 2
                    WHEN 'центральный полузащитник' THEN 3
                    WHEN 'нападающий' THEN 4
                END,
                sum_minutes DESC;
        """
        cursor.execute(get_players_query)
        players = cursor.fetchall()

        print("\nСписок игроков:")
        for player in players:
            print(player)

    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Вызываем функцию для выполнения задания № 1
task_1()

def create_views():
    try:
        connection = psycopg2.connect(
            database="my_pw_ls_71_db",
            host="localhost",
            user="postgres",
            password="admin",
            port="5432"
        )

        cursor = connection.cursor()

        # SQL-запрос для создания простого представления
        create_simple_view_query = """
            CREATE OR REPLACE VIEW Players_View AS
            SELECT * FROM Players;
        """
        cursor.execute(create_simple_view_query)
        connection.commit()

        # SQL-запрос для создания материализованного представления
        create_materialized_view_query = """
            CREATE MATERIALIZED VIEW Players_Materialized_View AS
            SELECT * FROM Players;
        """
        cursor.execute(create_materialized_view_query)
        connection.commit()

        print("Представления успешно созданы.")

    except psycopg2.Error as e:
        print("Ошибка:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Вызываем функцию для создания представлений
create_views()

def update_minutes():
    try:
        connection = psycopg2.connect(
            database="my_pw_ls_71_db",
            host="localhost",
            user="postgres",
            password="admin",
            port="5432"
        )

        cursor = connection.cursor()

        # SQL-запрос для обновления данных
        update_minutes_query = """
            UPDATE Players
            SET sum_minutes = 120
            WHERE nickname = 'А.Becker' AND player_number = 10;
        """
        cursor.execute(update_minutes_query)
        connection.commit()

        print("Количество минут обновлено.")

    except psycopg2.Error as e:
        print("Ошибка при обновлении данных:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Вызываем функцию для обновления количества минут
update_minutes()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг за шагом. Разбор кода, для Вас и для меня самого в будущем. Ведь я сейчас, не я через пол года.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг №1. Создание базы данных:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заглавление: Создание базы данных.

# Пример кода:

# def create_database():
#     try:
#         # Подключение к серверу PostgreSQL
#         connection = psycopg2.connect(
#             host="localhost",
#             user="postgres",
#             password="admin",
#             port="5432"
#         )
#
#         # Отключение автоматического запуска транзакций
#         connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
#
#         cursor = connection.cursor()
#
#         # Создание базы данных my_pw_ls_71_db, если она не существует
#         create_database_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier("my_pw_ls_71_db"))
#         cursor.execute(create_database_query)
#
#         print("База данных my_pw_ls_71_db успешно создана.")
#
#     except psycopg2.Error as e:
#         print("Ошибка при создании базы данных my_pw_ls_71_db:", e)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
# # Вызываем функцию для создания базы данных
# create_database()

# Описание:
# Этот код создает базу данных с названием "my_pw_ls_71_db" на сервере PostgreSQL,
# если такой базы данных еще не существует.


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг №2. Создание таблицы игроков:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заглавление: Создание таблицы игроков.

# Пример кода:

# def create_players_table():
#     try:
#         connection = psycopg2.connect(
#             database="my_pw_ls_71_db",
#             host="localhost",
#             user="postgres",
#             password="admin",
#             port="5432"
#         )
#
#         cursor = connection.cursor()
#
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS Players (
#                 id SERIAL PRIMARY KEY,
#                 nickname VARCHAR(50) NOT NULL,
#                 player_number INT NOT NULL,
#                 role VARCHAR(50) NOT NULL,
#                 citizenship VARCHAR(50) NOT NULL,
#                 sum_minutes INT NOT NULL,
#                 sum_cards INT NOT NULL
#             );
#         """
#         cursor.execute(create_table_query)
#         connection.commit()
#
#         print("Таблица Players успешно создана.")
#
#         # Добавим некоторые данные в таблицу
#         insert_data_query = """
#             INSERT INTO Players (nickname, player_number, role, citizenship, sum_minutes, sum_cards)
#             VALUES
#                 ('Ivan_Ivan', 1, 'голкипер', 'Russia', 90, 2),
#                 ('Rio_Carnavele', 2, 'защитник', 'Brazil', 90, 1),
#                 ('Hitler_Kaput', 3, 'нападающий', 'Germany', 90, 1),
#                 ('Ole_Ole_Ole', 4, 'нападающий', 'Argentina', 90, 0),
#                 ('Zorro', 5, 'центральный полузащитник', 'Spain', 90, 2),
#                 ('Kruasan', 6, 'голкипер', 'France', 90, 1),
#                 ('Spagetti_Borgia', 7, 'защитник', 'Italy', 90, 2),
#                 ('Big_Ben_Booom', 8, 'центральный полузащитник', 'England', 90, 1),
#                 ('Ronaldo', 9, 'голкипер', 'Portugal', 90, 0),
#                 ('А.Becker', 10, 'нападающий', 'Netherlands', 90, 1);
#         """
#         cursor.execute(insert_data_query)
#         connection.commit()
#
#         print("Данные успешно добавлены в таблицу Players.")
#
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
# # Создаем таблицу и добавляем данные
# create_players_table()

# Описание:
# Этот код создает таблицу "Players" в базе данных "my_pw_ls_71_db" и добавляет некоторые данные в эту таблицу.
# Таблица содержит информацию о футбольных игроках, такую как их псевдонимы, номера игроков, роли, гражданства,
# суммарное количество минут игры и количество желтых карточек.


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг №3. Выполнение задания № 1:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заглавление: Выполнение задания № 1.

# Пример кода:

# def task_1():
#     try:
#         connection = psycopg2.connect(
#             database="my_pw_ls_71_db",
#             host="localhost",
#             user="postgres",
#             password="admin",
#             port="5432"
#         )
#
#         cursor = connection.cursor()
#
#         # SQL-запрос для получения списка игроков с сортировкой
#         get_players_query = """
#             SELECT nickname, role, citizenship, sum_minutes, sum_cards
#             FROM Players
#             ORDER BY
#                 CASE role
#                     WHEN 'голкипер' THEN 1
#                     WHEN 'защитник' THEN 2
#                     WHEN 'центральный полузащитник' THEN 3
#                     WHEN 'нападающий' THEN 4
#                 END,
#                 sum_minutes DESC;
#         """
#         cursor.execute(get_players_query)
#         players = cursor.fetchall()
#
#         print("\nСписок игроков:")
#         for player in players:
#             print(player)
#
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
# # Вызываем функцию для выполнения задания № 1
# task_1()

# Описание:
# Этот код выполняет задание № 1, которое заключается в выводе списка игроков из таблицы "Players"
# в базе данных "my_pw_ls_71_db".
# Список игроков отсортирован по ролям (голкипер, защитник, центральный полузащитник, нападающий)
# и общему количеству минут игры в убывающем порядке.


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг №4. Создание представлений:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заглавление: Создание представлений.

# Пример кода:

# def create_views():
#     try:
#         connection = psycopg2.connect(
#             database="my_pw_ls_71_db",
#             host="localhost",
#             user="postgres",
#             password="admin",
#             port="5432"
#         )
#
#         cursor = connection.cursor()
#
#         # SQL-запрос для создания простого представления
#         create_simple_view_query = """
#             CREATE OR REPLACE VIEW Players_View AS
#             SELECT * FROM Players;
#         """
#         cursor.execute(create_simple_view_query)
#         connection.commit()
#
#         # SQL-запрос для создания материализованного представления
#         create_materialized_view_query = """
#             CREATE MATERIALIZED VIEW Players_Materialized_View AS
#             SELECT * FROM Players;
#         """
#         cursor.execute(create_materialized_view_query)
#         connection.commit()
#
#         print("Представления успешно созданы.")
#
#     except psycopg2.Error as e:
#         print("Ошибка:", e)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
# # Вызываем функцию для создания представлений
# create_views()

# Описание:
# Этот код создает два представления в базе данных "my_pw_ls_71_db".
# Первое представление является простым (не материализованным) и содержит все данные из таблицы "Players".
# Второе представление является материализованным и также содержит все данные из таблицы "Players".


# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Шаг №5. Обновление количества минут для игрока:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Заглавление: Обновление количества минут для игрока.

# Пример кода:

# def update_minutes():
#     try:
#         connection = psycopg2.connect(
#             database="my_pw_ls_71_db",
#             host="localhost",
#             user="postgres",
#             password="admin",
#             port="5432"
#         )
#
#         cursor = connection.cursor()
#
#         # SQL-запрос для обновления данных
#         update_minutes_query = """
#             UPDATE Players
#             SET sum_minutes = 120
#             WHERE nickname = 'А.Becker' AND player_number = 10;
#         """
#         cursor.execute(update_minutes_query)
#         connection.commit()
#
#         print("Количество минут обновлено.")
#
#     except psycopg2.Error as e:
#         print("Ошибка при обновлении данных:", e)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#
# # Вызываем функцию для обновления количества минут
# update_minutes()

# Описание:
# Этот код обновляет количество минут игры для игрока с псевдонимом 'А.Becker' и номером игрока 10 в таблице "Players".
# Новое количество минут установлено равным 120.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# СПАСИБО за внимание! Надеюсь, что Вы по достоинству оцените данную ПРАКТИЧЕСКУЮ РАБОТУ №8 - от 06.05.2024-07.05.2024