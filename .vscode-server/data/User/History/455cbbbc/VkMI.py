from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route ("/register_page")
def register_page_func():
    return render_template("Registro.html")

@app.route("/consult_page")
def consult_page_func():
    return "Vista de consultar"

if __name__ == "__main__":
    host = "172.31.36.89"
    port = ""
    app.run(host,port)