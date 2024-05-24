import psycopg2
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_db():
    try:
        return psycopg2.connect(
            dbname="myVODOMATs",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
    except psycopg2.OperationalError as e:
        logging.error(f"Ошибка подключения к базе данных: {e}")
        return None

def query_db(query, params=None, fetch=False):
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
    except psycopg2.IntegrityError as e:
        logging.error(f"Ошибка целостности данных: {e}")
        conn.rollback()
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        conn.rollback()
