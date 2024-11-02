from flask import Flask

app = Flask(__name__)

@app.route ("/register_page")
def register_page_func():
    return "Vista de registrar"
@app.route("/ consult_page")
def consult_page_func():
    return "Vista de consultar"

if __name__ == "__main__":
    host = "127.0.0.1"
    port = "3000"
    app.run(host,port)