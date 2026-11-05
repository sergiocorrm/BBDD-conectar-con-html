from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}


def conectar():
    return mysql.connector.connect(**CONFIG)


@app.route("/")
def inicio():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT nombre, usuario FROM usuarios")
    filas = cursor.fetchall()
    cursor.close()
    con.close()
    return render_template("index.html", usuarios=filas)


@app.route("/anadir", methods=["POST"])
def anadir():
    nombre = request.form["nombre"]
    usuario = request.form["usuario"]

    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, usuario) VALUES (%s, %s)",
                       (nombre, usuario))
        con.commit()
        cursor.close()
        con.close()
    except mysql.connector.IntegrityError:
        print("Ese usuario ya existe")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)