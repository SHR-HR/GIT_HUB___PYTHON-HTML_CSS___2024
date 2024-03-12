import MySQLdb
from flask import Flask, request, redirect

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="users_db")
cursor = db.cursor()


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Проверяем, существует ли пользователь с таким email
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    if user:
        return "Пользователь с таким email уже существует"

    # Хэшируем пароль
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Добавляем нового пользователя в базу данных
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                   (username, email, hashed_password))
    db.commit()

    return redirect('/login')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Получаем данные пользователя из базы данных
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
        # Вход пользователя прошел успешно, выполните необходимые действия
        return redirect('/dashboard')
    else:
        return "Неверные email или пароль"


if __name__ == '__main__':
    app.run(debug=True)
