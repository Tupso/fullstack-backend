""" Funcion para escribir el .txt """

def guardar_pedido(nombre, apellidos):
    """" Escribir el .txt """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
