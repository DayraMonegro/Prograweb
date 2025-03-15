from flask import Flask, render_template

app = Flask(_name_)
@app.route("/")
def index():
    return "Hola mundo desde flask"

@app.route("/bienvenida")
def bienvenida():
    return render_template("bienvenida.html")

@app.route("/Usuario")
def user(name):
    return f"<h1>hola{name}</h1>"

if __name__ == '_main_':
    app.run(debug=True)