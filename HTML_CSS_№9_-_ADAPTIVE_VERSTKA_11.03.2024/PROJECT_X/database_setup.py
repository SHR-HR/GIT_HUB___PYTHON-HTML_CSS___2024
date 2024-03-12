import mysql.connector

# Подключение к серверу MySQL (например, localhost)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Создание базы данных
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS users_db")
cursor.close()

# Подключение к созданной базе данных
conn.database = "users_db"

# Создание таблицы пользователей
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )
""")
cursor.close()

# Закрытие соединения с базой данных
conn.close()
