from flask import Flask, session, redirect, request, render_template

# Создаем приложение Flask
app = Flask(__name__)
# Настраиваем приложение Flask
# - Секретный код для сессий
app.config["SECRET_KEY"] = "secret_key"
# - Имя пользователя и пароль
app.config["USERNAME"] = "test"
app.config["PASSWORD"] = "test"

# Мы обрабатываем по данному URL и GET, и POST запрос
@app.route("/login/", methods=["GET", "POST"])
def login():
    # Если пользователь авторизован
    if session.get("is_auth"):
        # то редиректим его на приватную страницу
        return redirect("/")

    # Переменная для хранения ошибок авторизации
    error_msg = ""  # Пока ошибок нет

    # Пришел запрос на аутентификацию
    if request.method == "POST":

        # Получаем отправленные данные
        username = request.form.get("username")
        password = request.form.get("password")

        # Проверяем полученные данные
        if ((username and password) and username == app.config["USERNAME"] and password == app.config["PASSWORD"]):

            # Устанавливаем в сессии признак, что пользователь аутентифицирован
            session["is_auth"] = True

            # Редиректим пользователя на приватную страницу
            return redirect("/")

        else:

            error_msg = "Неверное имя или пароль"

    # Отображаем форму аутентификации
    return render_template("login/page_login.html")

app.run(debug=True, host='0.0.0.0', port=8080)