# Proyecto Web con Flask y Python

# Modulos a cargar

from flask import Flask, render_template, request
from datetime import datetime

# Inicio de la aplicacion web
app = Flask(__name__)

# Variables

# Funciones

# Funcion pagina principal
@app.route("/", methods=["GET", "POST"])
def home():
    # Variables
    result_1 = "0"
    result_2 = "0"
    operation = None
    resolved = 0
    # Metodo POST
    if request.method == "POST":
        result_1 = request.form["result_1"]
        result_2 = request.form["result_2"]
        operation = request.form["operation"]
        resolved = int(request.form["resolved"])
        if request.form.get("submit_button"):
            # Ingreso de numeros
            if request.form.get("submit_button") in "0123456789":
                if result_1[0] == "0" or resolved == 1:
                    result_1 = request.form.get("submit_button")
                elif resolved == 0:
                    result_1 += request.form.get("submit_button")
                resolved = 0
            # Ingreso de operaciones
            elif request.form.get("submit_button") in "+-X/":
                if operation != None and operation != "None":
                    if operation == "+":
                        result_1 = str(int(result_1) + int(result_2))
                    elif operation == "-":
                        result_1 = str(int(result_2) - int(result_1))
                    elif operation == "X":
                        result_1 = str(int(result_1) * int(result_2))
                    elif operation == "/":
                        result_1 = str(int(result_1) // int(result_2))
                    result_2 = "0"
                else:
                    result_2 = result_1
                    result_1 = "0"
                operation = request.form.get("submit_button")
            # Resultado
            elif request.form.get("submit_button") in "=":
                resolved = 1
                if result_2 != None and result_2 != "None":
                    if operation == "+":
                        result_1 = str(int(result_1) + int(result_2))
                    elif operation == "-":
                        result_1 = str(int(result_2) - int(result_1))
                    elif operation == "X":
                        result_1 = str(int(result_1) * int(result_2))
                    elif operation == "/":
                        result_1 = str(int(result_1) // int(result_2))
                else:
                    pass
                operation = None
            # Borrado
            elif request.form.get("submit_button") in "D":
                result_1 = "0"
                result_2 = "0"
                resolved = 0
                operation = None
    # Renderizado
    return render_template("index.html", result_1=result_1, 
                                        result_2=result_2, 
                                        operation=operation, 
                                        resolved=str(resolved))

# Main (debug=True para Desarrollo)

if __name__ == '__main__':
    app.run(port = 8000, debug=False, threaded=True)