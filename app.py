""" Generador de pedidos """

from flask import Flask, request, redirect, Response
import persistencia

app = Flask(__name__)
@app.route("/pizza",methods=['POST'])
def pizza():
    """ Obtener datos form y limpiar el .txt """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print(nombre)
    print(apellidos)

    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    persistencia.guardar_pedido(nombre, apellidos)

    return redirect("http://localhost/Front_Pizzas_FullStack/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """ Comprueba disponibilidad de un tamaño de pizza. """
    size = request.form.get("size")
    if size == "S":
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
