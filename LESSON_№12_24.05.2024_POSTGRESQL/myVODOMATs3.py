# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 18 МАЯ 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                              ДОМАШНЯЯ РАБОТА

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                            Дисциплина: Теория баз данных. PostgreSQL

                                        👇🏻 Выполните следующие задания:

👉🏻 Задание № 1.
Отправить логику проекта в питоне.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 17.05.2024 - учитель Марат Думан Ардакулы
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''👇🏻         ВАРИАНТ КОДА №3         👇🏻'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #

import psycopg2
from psycopg2 import OperationalError, IntegrityError
import logging

# Настройка логирования для отслеживания и вывода информации о процессах и ошибках
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_db():
    """ Устанавливает соединение с базой данных, обрабатывает возможные ошибки подключения. """
    try:
        return psycopg2.connect(
            dbname="myVODOMATs",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
    except OperationalError as e:
        logging.error(f"Ошибка подключения к базе данных: {e}")
        return None

def query_db(query, params=None, fetch=False):
    """
    Выполняет SQL запросы к базе данных.
    Обрабатывает различные исключения, связанные с выполнением запросов.
    Возвращает результаты для запросов на выборку данных.
    """
    conn = connect_db()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute(query, params)
        if fetch:
            result = cur.fetchall()
            cur.close()
            conn.close()
            return result
        else:
            conn.commit()
            cur.close()
            conn.close()
    except IntegrityError as e:
        logging.error(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        conn.rollback()

def create_vending_machine(location, status, install_date):
    """
    Добавляет новый водомат в базу данных.
    Логирует процесс добавления для подтверждения успешного выполнения.
    """
    try:
        query_db("INSERT INTO vending_machines (location, status, installation_date) VALUES (%s, %s, %s)",
                 (location, status, install_date))
        logging.info(f"Водомат добавлен: {location}, статус - {status}, дата установки - {install_date}")
    except Exception as e:
        logging.error(f"Не удалось добавить водомат: {e}")

def get_vending_machines():
    """
    Получает список всех водоматов из базы данных и выводит их в консоль.
    """
    machines = query_db("SELECT * FROM vending_machines", fetch=True)
    logging.info("Запрос списка всех водоматов выполнен.")
    for machine in machines:
        print(machine)
    return machines

def update_vending_machine(id, status):
    """
    Обновляет статус водомата по его ID.
    Логирует процесс обновления.
    """
    query_db("UPDATE vending_machines SET status = %s WHERE id = %s", (status, id))
    logging.info(f"Статус водомата с ID {id} обновлен на {status}")

def delete_vending_machine(id):
    """
    Удаляет водомат и связанные записи в инвентаре.
    Логирует процесс удаления для подтверждения.
    """
    query_db("DELETE FROM inventory WHERE vending_machine_id = %s", (id,))
    query_db("DELETE FROM vending_machines WHERE id = %s", (id,))
    logging.info(f"Водомат с ID {id} и связанные записи удалены")

def main():
    """ Основная функция для демонстрации использования функций управления базой данных. """
    create_vending_machine('Новый адрес', 'active', '2024-01-01')
    machines = get_vending_machines()
    update_vending_machine(1, 'maintenance')
    delete_vending_machine(1)

if __name__ == "__main__":
    main()

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#   Я ПОДУМАЛ, БЫЛО БЫ ПОЛЕЗНО ДЛЯ СЕБЯ (ну и в целом, для Вас - расписать код, попытаться его разобрать по шагам).   #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #

# Шаг №1. - Импорт библиотек и настройка логирования

# import psycopg2
# from psycopg2 import OperationalError, IntegrityError
# import logging

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# import psycopg2: Импорт библиотеки psycopg2, которая позволяет взаимодействовать с базой данных PostgreSQL.
# from psycopg2 import OperationalError, IntegrityError: Импорт двух исключений (OperationalError и IntegrityError),
# которые могут возникнуть при работе с базой данных.
# import logging: Импорт модуля logging для ведения журнала событий.



# Шаг №2. - Функция connect_db()

# def connect_db():
#     """ Устанавливает соединение с базой данных, обрабатывает возможные ошибки подключения. """
#     try:
#         return psycopg2.connect(
#             dbname="myVODOMATs",
#             user="postgres",
#             password="admin",
#             host="localhost",
#             port="5432"
#         )
#     except OperationalError as e:
#         logging.error(f"Ошибка подключения к базе данных: {e}")
#         return None

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# def connect_db():: Объявление функции connect_db, которая устанавливает соединение с базой данных PostgreSQL.
# """ Устанавливает соединение с базой данных, обрабатывает возможные ошибки подключения. """: Краткое описание функции.
# try: ... except OperationalError as e: ...: Блок try-except для обработки возможных ошибок подключения к базе данных.
# Если происходит ошибка OperationalError, она будет залогирована.



# Шаг №3. - Функция query_db()

# def query_db(query, params=None, fetch=False):
#     """
#     Выполняет SQL запросы к базе данных.
#     Обрабатывает различные исключения, связанные с выполнением запросов.
#     Возвращает результаты для запросов на выборку данных.
#     """
#     conn = connect_db()
#     if conn is None:
#         return
#     try:
#         cur = conn.cursor()
#         cur.execute(query, params)
#         if fetch:
#             result = cur.fetchall()
#             cur.close()
#             conn.close()
#             return result
#         else:
#             conn.commit()
#             cur.close()
#             conn.close()
#     except IntegrityError as e:
#         logging.error(f"Ошибка целостности данных: {e}")
#         conn.rollback()
#     except Exception as e:
#         logging.error(f"Произошла ошибка: {e}")
#         conn.rollback()

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# def query_db(query, params=None, fetch=False):: Объявление функции query_db,
# которая выполняет SQL-запросы к базе данных.
# """ Выполняет SQL запросы к базе данных... """: Документационная строка, описывающая функцию.
# conn = connect_db(): Устанавливаем соединение с базой данных с помощью функции connect_db.
# try: ... except IntegrityError as e: ... except Exception as e: ...: Обработка исключений при выполнении запросов.
# Если возникают ошибки IntegrityError, они логируются и выполняется откат изменений (rollback).
# Общие ошибки логируются также, и также выполняется откат изменений.



# Шаг №4. - Функция create_vending_machine()

# def create_vending_machine(location, status, install_date):
#     """
#     Добавляет новый водомат в базу данных.
#     Логирует процесс добавления для подтверждения успешного выполнения.
#     """
#     try:
#         query_db("INSERT INTO vending_machines (location, status, installation_date) VALUES (%s, %s, %s)",
#                  (location, status, install_date))
#         logging.info(f"Водомат добавлен: {location}, статус - {status}, дата установки - {install_date}")
#     except Exception as e:
#         logging.error(f"Не удалось добавить водомат: {e}")

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# def create_vending_machine(location, status, install_date)::
# Объявление функции create_vending_machine, которая добавляет новый водомат в базу данных.
# """ Добавляет новый водомат в базу данных... """: Документационная строка, описывающая функцию.
# try: ... except Exception as e: ...: Блок try-except для обработки возможных ошибок при добавлении водомата.
# Если происходит ошибка, она логируется.



# Шаг №5. - Функция get_vending_machines()

# def get_vending_machines():
#     """
#     Получает список всех водоматов из базы данных и выводит их в консоль.
#     """
#     machines = query_db("SELECT * FROM vending_machines", fetch=True)
#     logging.info("Запрос списка всех водоматов выполнен.")
#     for machine in machines:
#         print(machine)
#     return machines

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# def get_vending_machines():: Объявление функции get_vending_machines,
# которая получает список всех водоматов из базы данных и выводит их в консоль.
# """ Получает список всех водоматов из базы данных и выводит их в консоль... """:
# Документационная строка, описывающая функцию.
# machines = query_db("SELECT * FROM vending_machines", fetch=True):
# Выполнение SQL-запроса для получения всех записей из таблицы vending_machines.
# Результат сохраняется в переменную machines.
# logging.info("Запрос списка всех водоматов выполнен."): Логирование успешного выполнения запроса.



# Шаг №6. - Функция update_vending_machine()

# def update_vending_machine(id, status):
#     """
#     Обновляет статус водомата по его ID.
#     Логирует процесс обновления.
#     """
#     query_db("UPDATE vending_machines SET status = %s WHERE id = %s", (status, id))
#     logging.info(f"Статус водомата с ID {id} обновлен на {status}")

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# def update_vending_machine(id, status):: Объявление функции update_vending_machine,
# которая обновляет статус водомата по его идентификатору.
# """ Обновляет статус водомата по его ID... """: Документационная строка, описывающая функцию.
# query_db("UPDATE vending_machines SET status = %s WHERE id = %s", (status, id)):
# Выполнение SQL-запроса для обновления статуса водомата. Значения заменяются на переданные параметры status и id.
# logging.info(f"Статус водомата с ID {id} обновлен на {status}"): Логирование успешного обновления статуса водомата.



# Шаг №7. - Функция delete_vending_machine()

# def delete_vending_machine(id):
#     """
#     Удаляет водомат и связанные записи в инвентаре.
#     Логирует процесс удаления для подтверждения.
#     """
#     query_db("DELETE FROM inventory WHERE vending_machine_id = %s", (id,))
#     query_db("DELETE FROM vending_machines WHERE id = %s", (id,))
#     logging.info(f"Водомат с ID {id} и связанные записи удалены")

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# def delete_vending_machine(id):: Объявление функции delete_vending_machine,
# которая удаляет водомат и связанные с ним записи в инвентаре.
# """ Удаляет водомат и связанные записи в инвентаре... """: Документационная строка, описывающая функцию.
# query_db("DELETE FROM inventory WHERE vending_machine_id = %s", (id,)): Выполнение SQL-запроса для удаления
# записей в инвентаре, связанных с водоматом, по его идентификатору.
# query_db("DELETE FROM vending_machines WHERE id = %s", (id,)):
# Выполнение SQL-запроса для удаления водомата по его идентификатору.
# logging.info(f"Водомат с ID {id} и связанные записи удалены"):
# Логирование успешного удаления водомата и связанных с ним записей.



# Шаг №8. - Функция main()

# def main():
#     """ Основная функция для демонстрации использования функций управления базой данных. """
#     create_vending_machine('Новый адрес', 'active', '2024-01-01')
#     machines = get_vending_machines()
#     update_vending_machine(1, 'maintenance')
#     delete_vending_machine(1)

# Описание:
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# def main():: Объявление функции main, которая служит для демонстрации использования функций управления базой данных.
# """ Основная функция для демонстрации использования функций управления базой данных. """:
# Документационная строка, описывающая функцию.
# create_vending_machine('Новый адрес', 'active', '2024-01-01'):
# Вызов функции create_vending_machine() для добавления нового водомата в базу данных.
# machines = get_vending_machines():
# Вызов функции get_vending_machines() для получения списка всех водоматов из базы данных.
# update_vending_machine(1, 'maintenance'):
# Вызов функции update_vending_machine() для обновления статуса водомата с идентификатором 1 на 'maintenance'.
# delete_vending_machine(1):
# Вызов функции delete_vending_machine() для удаления водомата с идентификатором 1.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Итак, весь код предназначен для работы с базой данных,
# в которой хранится информация о водоматах. Функции позволяют добавлять новые водоматы,
# получать список всех водоматов, обновлять статус водомата и удалять водомат из базы данных.
# Логирование используется для отслеживания процессов и ошибок,
# что обеспечивает более удобное отладочное управление кодом.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# Источник: google & habr-habr (reddit & github)
