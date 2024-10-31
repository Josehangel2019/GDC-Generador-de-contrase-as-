from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generar_contraseña(longitud, mayusculas, numeros, simbolos):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    return ''.join(random.choice(caracteres) for _ in range(longitud))

@app.route("/", methods=["GET", "POST"])
def index():
    contraseña = None
    if request.method == "POST":
        longitud = int(request.form.get("longitud"))
        mayusculas = request.form.get("mayusculas") == "on"
        numeros = request.form.get("numeros") == "on"
        simbolos = request.form.get("simbolos") == "on"
        contraseña = generar_contraseña(longitud, mayusculas, numeros, simbolos)
    return render_template("index.html", contraseña=contraseña)

if __name__ == "__main__":
    app.run(debug=True)
