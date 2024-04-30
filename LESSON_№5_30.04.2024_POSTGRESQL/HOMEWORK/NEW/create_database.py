import psycopg2


connect =  psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
) 
connect.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cur =  connect.cursor()
cur.execute(
        """
CREATE DATABASE work_db;
""")