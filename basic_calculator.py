# Proyecto Web con Flask y Python

# Modulos a cargar

from flask import Flask, render_template, request

# Inicio de la aplicacion web
app = Flask(__name__)

# Funciones
# Funcion pagina principal
@app.route("/", methods=["GET", "POST"])
def home():
    # Variables
    result_1 = "0"
    result_2 = "0"
    operation = None
    resolved = 0
    visor_calc = ""
    # Metodo POST
    if request.method == "POST":
        result_1 = request.form["result_1"]
        result_2 = request.form["result_2"]
        operation = request.form["operation"]
        visor_calc = request.form["visor_calc"]
        resolved = int(request.form["resolved"])
        print(result_1, result_2)
        if request.form.get("submit_button"):
            # Ingreso de numeros
            if request.form.get("submit_button") in "0123456789,":
                if result_1[0] == "0" or resolved == 1:
                    result_1 = request.form.get("submit_button")
                elif resolved == 0:
                    if request.form.get("submit_button") == ",":
                        if result_1.find(".") == -1:
                            result_1 += "."
                    else:
                        result_1 += request.form.get("submit_button")
                resolved = 0
            # Ingreso de operaciones
            elif request.form.get("submit_button") in "+-X/":
                if operation != None and operation != "None":
                    if operation == "+":
                        result_1 = str(float(result_1) + float(result_2))
                    elif operation == "-":
                        result_1 = str(float(result_2) - float(result_1))
                    elif operation == "X":
                        result_1 = str(float(result_1) * float(result_2))
                    elif operation == "/":
                        result_1 = str(float(result_2) / float(result_1))
                    result_2 = "0"
                    visor_calc = ""
                else:
                    result_2 = result_1
                    visor_calc = result_1 + " " + request.form.get("submit_button")
                    result_1 = "0"
                operation = request.form.get("submit_button")
            # Resultado
            elif request.form.get("submit_button") in "=":
                resolved = 1
                if result_2 != None and result_2 != "None":
                    if operation == "+":
                        result_1 = str(float(result_1) + float(result_2))
                    elif operation == "-":
                        result_1 = str(float(result_2) - float(result_1))
                    elif operation == "X":
                        result_1 = str(float(result_1) * float(result_2))
                    elif operation == "/":
                        result_1 = str(float(result_2) / float(result_1))
                    result_2 = "0"
                    visor_calc = ""
                else:
                    pass
                operation = None
            # Borrado
            elif request.form.get("submit_button") in "D":
                result_1 = "0"
                result_2 = "0"
                resolved = 0
                visor_calc = ""
                operation = None
            elif request.form.get("submit_button") in "C":
                result_1 = "0"
    # Renderizado
    return render_template("index.html", result_1=result_1, 
                                        result_2=result_2, 
                                        operation=operation, 
                                        visor_calc=visor_calc,
                                        resolved=str(resolved))

# Main (debug=True para Desarrollo)

if __name__ == '__main__':
    app.run(port = 8000, debug=True, threaded=True)