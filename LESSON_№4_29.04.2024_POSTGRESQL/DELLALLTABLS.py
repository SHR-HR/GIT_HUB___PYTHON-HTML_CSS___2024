import psycopg2

try:
    # Подключение к базе данных
    connect = psycopg2.connect(
        dbname="LESSON_№4_29.04.2024_POSTGRESQL",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )

    # Удаление всех таблиц
    with connect.cursor() as cur:
        cur.execute("DROP SCHEMA public CASCADE")
        cur.execute("CREATE SCHEMA public")
        connect.commit()

    print("Все таблицы были успешно удалены.")

    # Закрыть подключение к базе данных
    connect.close()

except psycopg2.Error as e:
    print("Ошибка при подключении к базе данных:", e)

