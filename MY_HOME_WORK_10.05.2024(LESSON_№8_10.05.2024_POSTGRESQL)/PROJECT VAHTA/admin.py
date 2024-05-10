# 11.05.2024.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Чуть-чуть доработал код для его запуска в основном в PyCharm.
# Для того чтобы остановить выполнение запуска кода нажимайте CTRL+F2 (в VS CODE это CTRL+C).
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Домашняя Работа от 10.05.2024 - "Реализовать выгрузку за месяц и за сегодня" P.S. Сделать в ексель выгрузку).
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ВАРИАНТ КОДА №3 - Полностью Выполняет ДОМАШНЕЕ ЗАДАНИЕ от 10.05.2024 - Lesson №8

import psycopg2
from datetime import datetime, date
from openpyxl import Workbook

def get_worked_hours(start_date, end_date):
    conn = psycopg2.connect(
        dbname="my_vahta",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    sql_query = """
        SELECT user_name, SUM(time_outo - time_into) AS worked_interval
        FROM work_time
        JOIN users USING(user_id)
        WHERE DATE(time_into) BETWEEN %s AND %s
        GROUP BY user_name;
    """
    cur.execute(sql_query, (start_date, end_date))

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results

def export_to_excel(data, filename):
    wb = Workbook()
    ws = wb.active
    ws.append(["Сотрудник", "Отработано секунд"])

    for row in data:
        ws.append(row)

    wb.save(filename)

def main():
    period_choice = input("За какой период вы хотите получить выгрузку?\n"
                          "1. За сегодня?\n"
                          "2. За ТЕКУЩИЙ месяц?\n"
                          "3. Свой промежуток времени?\n"
                          "Введите номер варианта: ")

    current_date = date.today()

    if period_choice == "1":
        start_date = current_date
        end_date = current_date
        filename = "Выгрузка 1.xlsx"
    elif period_choice == "2":
        start_date = current_date.replace(day=1)
        end_date = current_date
        filename = "Выгрузка 2.xlsx"
    elif period_choice == "3":
        start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
        end_date = input("Введите конечную дату (ГГГГ-ММ-ДД): ")
        filename = "Выгрузка 3.xlsx"
    else:
        print("Некорректный выбор периода")
        return

    data = get_worked_hours(start_date, end_date)
    export_to_excel(data, filename)

if __name__ == "__main__":
    main()









# ВАРИАНТ КОДА №2 - Так как это уже Домашняя работа - то, я продолжил дорабатывать первый Вариант кода.

# import psycopg2
# from datetime import date
#
# # Подключение к базе данных
# conn = psycopg2.connect(
#     dbname="my_vahta",
#     user="postgres",
#     password="admin",
#     host="localhost",
#     port="5432"
# )
#
# # Открытие курсора
# cur = conn.cursor()
#
# # Запрос у пользователя, за какой период он хочет получить выгрузку
# print("За какой период Вы хотите получить выгрузку? Пожалуйста выберите подходящий для Вас вариант:")
# print("1. За сегодня?")
# print("2. За ТЕКУЩИЙ месяц?")
# print("3. Свой промежуток времени?")
# period_choice = input("Введите номер варианта: ")
#
# # Получение текущей даты
# current_date = date.today()
#
# # SQL-запрос для подсчёта отработанных секунд каждым сотрудником за выбранный период
# if period_choice == "1":
#     sql_query = """
#         SELECT user_name, SUM(time_outo - time_into) AS worked_interval
#         FROM work_time
#         JOIN users USING(user_id)
#         WHERE DATE(time_into) = %s
#         GROUP BY user_name;
#     """
#     # Выполнение запроса с параметром текущей даты
#     cur.execute(sql_query, (current_date,))
# elif period_choice == "2":
#     current_month = current_date.replace(day=1)
#     sql_query = """
#         SELECT user_name, SUM(time_outo - time_into) AS worked_interval
#         FROM work_time
#         JOIN users USING(user_id)
#         WHERE DATE_TRUNC('month', time_into) = %s
#         GROUP BY user_name;
#     """
#     # Выполнение запроса с параметром текущего месяца
#     cur.execute(sql_query, (current_month,))
# elif period_choice == "3":
#     start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
#     end_date = input("Введите конечную дату (ГГГГ-ММ-ДД): ")
#     sql_query = """
#         SELECT user_name, SUM(time_outo - time_into) AS worked_interval
#         FROM work_time
#         JOIN users USING(user_id)
#         WHERE DATE(time_into) BETWEEN %s AND %s
#         GROUP BY user_name;
#     """
#     # Выполнение запроса с параметрами начальной и конечной даты
#     cur.execute(sql_query, (start_date, end_date))
# else:
#     print("Некорректный выбор периода")
#     cur.close()
#     conn.close()
#     exit()
#
# # Получение результатов
# results = cur.fetchall()
#
# # Вывод результатов
# for row in results:
#     user_name, worked_interval = row
#     print(f"Сотрудник {user_name} отработал {worked_interval} секунд.")
#
# # Закрытие курсора и соединения
# cur.close()
# conn.close()





# ВАРИАНТ КОДА №1 (Начал его исполнять практически в конце 2-ой пары) - 10.05.2024

# import psycopg2
#
# # Подключение к базе данных
# conn = psycopg2.connect(
#     dbname="my_vahta",
#     user="postgres",
#     password="admin",
#     host="localhost",
#     port="5432"
# )
#
# # Открытие курсора
# cur = conn.cursor()
#
# # SQL-запрос для подсчёта отработанных секунд каждым сотрудником за сегодня
# sql_query = """
#     SELECT user_name, SUM(time_outo - time_into) AS worked_interval
#     FROM work_time
#     JOIN users USING(user_id)
#     WHERE DATE(time_into) = CURRENT_DATE
#     GROUP BY user_name;
# """
#
# # Выполнение запроса
# cur.execute(sql_query)
#
# # Получение результатов
# results = cur.fetchall()
#
# # Вывод результатов
# for row in results:
#     user_name, worked_interval = row
#     print(f"Сотрудник {user_name} отработал {worked_interval} секунд сегодня.")
#
# # Закрытие курсора и соединения
# cur.close()
# conn.close()