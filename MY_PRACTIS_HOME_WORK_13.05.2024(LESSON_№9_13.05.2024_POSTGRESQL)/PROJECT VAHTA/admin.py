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
