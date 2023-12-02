from flask import Flask, request, redirect

app = Flask(__name__)
@app.route("/pizza",methods=['POST'])
def pizza():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print(nombre)
    print(apellidos)

    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    guardar_pedido(nombre, apellidos)

    return redirect("http://localhost/Front_Pizzas_FullStack/solicita_pedido.html", code=302)

def guardar_pedido(nombre, apellidos):
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos)
        file.close()



