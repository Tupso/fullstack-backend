""" Generador de pedidos """

from flask import Flask, request, redirect
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
