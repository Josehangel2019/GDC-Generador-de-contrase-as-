from flask import Flask, render_template, request  # Importamos Flask y funciones útiles.
import random
import string

app = Flask(__name__)  # Inicializamos la app Flask.

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=False):
    caracteres = string.ascii_lowercase  # Iniciamos con letras minúsculas.
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Añadimos mayúsculas si se selecciona.
    if incluir_numeros:
        caracteres += string.digits  # Añadimos números.
    if incluir_simbolos:
        caracteres += string.punctuation  # Añadimos símbolos.

    # Generamos la contraseña con caracteres aleatorios.
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

@app.route("/", methods=["GET", "POST"])  # Ruta para la página principal.
def index():
    contraseña = ""  # Variable para la contraseña generada.
    if request.method == "POST":  # Si el usuario envía el formulario:
        longitud = int(request.form["longitud"])
        incluir_mayusculas = "mayusculas" in request.form
        incluir_numeros = "numeros" in request.form
        incluir_simbolos = "simbolos" in request.form

        # Llamamos a la función para generar la contraseña.
        contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)

    return render_template("index.html", contraseña=contraseña)

if __name__ == "__main__":
    app.run(debug=True)  # Iniciamos la app en modo depuración.
