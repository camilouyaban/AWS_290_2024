from flask import Flask, render_template
from database import * 
app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route ("/home/ec2-user/templates/Registro.html")
def register_page_func():
    return render_template("Registro.html")

@app.route("/Registo_usuario", methods=["post"])
def register_render_func():
    return "Comentario enviado"

@app.route("/consult_page")
def consult_page_func():
    return "Vista de consultar"

if __name__ == "__main__":
    host = "172.31.36.89"
    port = "80"
    app.run(host,port)