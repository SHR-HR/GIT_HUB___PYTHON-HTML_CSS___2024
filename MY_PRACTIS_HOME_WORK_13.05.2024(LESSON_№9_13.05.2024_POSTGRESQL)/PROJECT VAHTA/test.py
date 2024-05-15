# 14.05.2024.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Практическая Работа от 13.05.2024
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Практическая работа - вариант кода №2


import psycopg2
import os
import subprocess


def create_files_table():
    """Создает таблицу files в базе данных."""
    try:
        conn = psycopg2.connect(
            dbname="my_vahta",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS files (
                file_id SERIAL PRIMARY KEY,
                file_name VARCHAR(200),
                file_data BYTEA,
                file_type VARCHAR(50),
                file_size BIGINT
            );
        """)
        conn.commit()
        print("Таблица files успешно создана.")

    except psycopg2.Error as e:
        print("Ошибка при создании таблицы files:", e)

    finally:
        cur.close()
        conn.close()


def insert_file_into_database(file_path):
    """Загружает файл в базу данных."""
    try:
        conn = psycopg2.connect(
            dbname="my_vahta",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        file_name = os.path.basename(file_path)
        file_type = os.path.splitext(file_name)[1][1:]
        file_size = os.path.getsize(file_path)

        with open(file_path, 'rb') as file:
            file_data = file.read()

        cur.execute("""
            INSERT INTO files (file_name, file_data, file_type, file_size)
            VALUES (%s, %s, %s, %s);
        """, (file_name, file_data, file_type, file_size))
        conn.commit()
        print(f"Файл {file_name} успешно загружен в базу данных.")

    except psycopg2.Error as e:
        print("Ошибка при загрузке файла в базу данных:", e)

    finally:
        cur.close()
        conn.close()


def main():
    create_files_table()

    file_list = [
        "example.jpg",
        "example.mp3",
        "example.mp4"
    ]

    for file_path in file_list:
        insert_file_into_database(file_path)

    choice = input("Не желаете ли вы просмотреть загруженные файлы? (1 - да, 2 - нет): ")
    if choice == "1":
        downloaded_files_path = os.path.join(os.getcwd(), "downloaded_files")  # Получаем полный путь к папке
        if not os.path.exists(downloaded_files_path):
            os.makedirs(downloaded_files_path)

        conn = psycopg2.connect(
            dbname="my_vahta",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM files;")
        files = cur.fetchall()
        cur.close()
        conn.close()

        for file in files:
            file_name, file_data, file_type = file[1], file[2], file[3]
            file_path = os.path.join(downloaded_files_path, file_name)
            with open(file_path, "wb") as f:
                f.write(file_data)

            subprocess.run([file_path], shell=True)


if __name__ == "__main__":
    main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Если хотите, можете "разкоментировать" код.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Практическая работа - вариант кода №1 - Доработанный


# import psycopg2
# import os
# import subprocess
#
#
# def create_files_table():
#     """Создает таблицу files в базе данных."""
#     try:
#         conn = psycopg2.connect(
#             dbname="my_vahta",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor()
#
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS files (
#                 file_id SERIAL PRIMARY KEY,
#                 file_name VARCHAR(200),
#                 file_data BYTEA,
#                 file_type VARCHAR(50)
#             );
#         """)
#         conn.commit()
#         print("Таблица files успешно создана.")
#
#     except psycopg2.Error as e:
#         print("Ошибка при создании таблицы files:", e)
#
#     finally:
#         cur.close()
#         conn.close()
#
#
# def insert_file_into_database(file_path):
#     """Загружает файл в базу данных."""
#     try:
#         conn = psycopg2.connect(
#             dbname="my_vahta",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor()
#
#         file_name = os.path.basename(file_path)
#         file_type = os.path.splitext(file_name)[1][1:]
#
#         with open(file_path, 'rb') as file:
#             file_data = file.read()
#
#         cur.execute("""
#             INSERT INTO files (file_name, file_data, file_type)
#             VALUES (%s, %s, %s);
#         """, (file_name, file_data, file_type))
#         conn.commit()
#         print(f"Файл {file_name} успешно загружен в базу данных.")
#
#     except psycopg2.Error as e:
#         print("Ошибка при загрузке файла в базу данных:", e)
#
#     finally:
#         cur.close()
#         conn.close()
#
#
# def main():
#     create_files_table()
#
#     file_list = [
#         "example.jpg",
#         "example.mp3",
#         "example.mp4"
#     ]
#
#     for file_path in file_list:
#         insert_file_into_database(file_path)
#
#     choice = input("Не желаете ли вы просмотреть загруженные файлы? (1 - да, 2 - нет): ")
#     if choice == "1":
#         conn = psycopg2.connect(
#             dbname="my_vahta",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM files;")
#         files = cur.fetchall()
#         cur.close()
#         conn.close()
#
#         if not os.path.exists("downloaded_files"):
#             os.makedirs("downloaded_files")
#
#         for file in files:
#             file_name, file_data, file_type = file[1], file[2], file[3]
#             file_path = os.path.join("downloaded_files", file_name)  # Путь для сохранения скачанных файлов
#             with open(file_path, "wb") as f:
#                 f.write(file_data)
#
#             subprocess.run([file_path], shell=True)  # Открывает файл с помощью программы по умолчанию
#
#
# if __name__ == "__main__":
#     main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Если хотите, можете "разкоментировать" код.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Практическая работа - вариант кода №1


# import psycopg2
# import os
#
# def create_files_table():
#     """Создает таблицу files в базе данных."""
#     try:
#         conn = psycopg2.connect(
#             dbname="my_vahta",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor()
#
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS files (
#                 file_id SERIAL PRIMARY KEY,
#                 file_name VARCHAR(200),
#                 file_data BYTEA,
#                 file_type VARCHAR(50)
#             );
#         """)
#         conn.commit()
#         print("Таблица files успешно создана.")
#
#     except psycopg2.Error as e:
#         print("Ошибка при создании таблицы files:", e)
#
#     finally:
#         cur.close()
#         conn.close()
#
# def insert_file_into_database(file_path):
#     """Загружает файл в базу данных."""
#     try:
#         conn = psycopg2.connect(
#             dbname="my_vahta",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#         )
#         cur = conn.cursor()
#
#         file_name = os.path.basename(file_path)
#         file_type = os.path.splitext(file_name)[1][1:]
#
#         with open(file_path, 'rb') as file:
#             file_data = file.read()
#
#         cur.execute("""
#             INSERT INTO files (file_name, file_data, file_type)
#             VALUES (%s, %s, %s);
#         """, (file_name, file_data, file_type))
#         conn.commit()
#         print(f"Файл {file_name} успешно загружен в базу данных.")
#
#     except psycopg2.Error as e:
#         print("Ошибка при загрузке файла в базу данных:", e)
#
#     finally:
#         cur.close()
#         conn.close()
#
# def main():
#     create_files_table()
#
#     file_list = [
#         "example.jpg",
#         "example.mp3",
#         "example.mp4"
#     ]
#
#     for file_path in file_list:
#         insert_file_into_database(file_path)
#
# if __name__ == "__main__":
#     main()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Практика кода во время пары:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import psycopg2
# from PIL import Image
#
# with psycopg2.connect(
#         dbname="my_vahta",
#         user="postgres",
#         password="admin",
#         host="localhost",
#         port="5432"
# ) as connect:
#     with connect.cursor() as cur:
#         cur.execute('''SELECT * FROM fiels''')
#         data = cur.fetchall()
#         img = Image.open(data[0][3])
#         img.show()
#         print(data)
#
#     with connect.cursor() as cur:
#         cur.execute(f'INSERT INTO fiels (file_name, file_path) VALUES (\'download.jpg\', \'.\\download.png\')')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Если хотите, можете "разкоментировать" код.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Старт - первые строчки.

# import psycopg2
# from psycopg2 import sql
# import os
#
#
# def upload_file_to_database(file_path, conn):
#     try:
#         # Открываем файл для бинарного чтения
#         with open(file_path, 'rb') as file:
#             file_data = file.read()
#
#         # Определяем имя файла
#         file_name = os.path.basename(file_path)
#
#         # Создаем SQL-запрос для вставки файла в базу данных
#         insert_query = sql.SQL("""
#             INSERT INTO files (file_name, file_data)
#             VALUES (%s, %s)
#             RETURNING file_id;
#         """)
#
#         # Выполняем запрос с данными файла
#         with conn.cursor() as cur:
#             cur.execute(insert_query, (file_name, file_data))
#             file_id = cur.fetchone()[0]
#             conn.commit()
#
#         print(f"Файл '{file_name}' успешно загружен в базу данных с ID {file_id}")
#
#     except Exception as e:
#         print(f"Ошибка при загрузке файла '{file_path}' в базу данных: {e}")
#
#
# def main():
#     try:
#         # Подключаемся к базе данных PostgreSQL
#         conn = psycopg2.connect(
#             dbname="my_vahta",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#         )
#
#         # Загружаем файлы в базу данных
#         upload_file_to_database("example.jpg", conn)
#         upload_file_to_database("example.mp3", conn)
#         upload_file_to_database("example.mp4", conn)
#
#     except Exception as e:
#         print(f"Ошибка подключения к базе данных: {e}")
#
#     finally:
#         # Закрываем соединение с базой данных
#         if conn:
#             conn.close()
#
#
# if __name__ == "__main__":
#     main()
