
import os
from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "local-development-key")

USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
PASSWORD = os.environ.get("ADMIN_PASSWORD", "kalibrasi123")

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            session["login"] = True
            return redirect("/dashboard")
        else:
            error = "Username atau password salah"

    return render_template_string("""
    <html>
    <head>
        <title>Login Dashboard Kalibrasi</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial;
                background: #eef2f7;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .box {
                background: white;
                padding: 30px;
                border-radius: 12px;
                width: 320px;
            }
            input, button {
                width: 100%;
                padding: 12px;
                margin-top: 12px;
                box-sizing: border-box;
            }
            button {
                background: #123b68;
                color: white;
                border: none;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Dashboard Kalibrasi</h2>
            <form method="POST">
                <input name="username" placeholder="Username" required>
                <input name="password" type="password"
                       placeholder="Password" required>
                <button type="submit">LOGIN</button>
            </form>
            <p style="color:red">{{ error }}</p>
        </div>
    </body>
    </html>
    """, error=error)

@app.route("/dashboard")
def dashboard():
    if not session.get("login"):
        return redirect("/")

    return """
    <h1>Dashboard Kalibrasi</h1>
    <p>Monitoring alat ukur dan jadwal kalibrasi</p>
    <a href="/logout">Logout</a>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run()
