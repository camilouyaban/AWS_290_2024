from flask import Flask, render_template, request
from database.db import add_user
app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def register_page_func():
    return render_template("Registro.html")

@app.route("/Registo_usuario", methods=["POST"])
def register_render_func():
    data = request.form
    id = data["Id"]  
    Nombre = data["Nombre"]
    Apellido = data["Apellido"]
    Cumpleaños = data["Fecha de nacimiento"]
    Telefono = data["Numero telefónico"]
    Comentario = data["Comentario"]
    add_user(id, Nombre, Apellido, Cumpleaños, Telefono, Comentario)
    return "Comentario enviado"

@app.route("/consult_page")
def consult_page_func():
    return "Vista de consultar"

if __name__ == "__main__":
    host = "172.31.36.89"
    port = "80"
    app.run(host,port)