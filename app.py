from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
productos = [
    {
        "id": 1,
        "nombre": "Computador",
        "precio": 2500000,
        "cantidad": 5
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 50000,
        "cantidad": 10
    },
    {
        "id": 3,
        "nombre": "Teclado",
        "precio": 120000,
        "cantidad": 8
    }
]


@app.route("/", methods=["GET"])
def mostrar_inicio():
    """
    Muestra un mensaje de bienvenida a la API.

    Parámetros:
        No recibe parámetros.

    Retorna:
        JSON: Mensaje de bienvenida.
    """
    return jsonify({
        "mensaje": "Bienvenido a API_TIENDA"
    })


@app.route("/productos", methods=["GET"])
def consultar_productos():
    """
    Consulta todos los productos registrados.

    Parámetros:
        No recibe parámetros.

    Retorna:
        JSON: Lista de productos registrados.
    """
    return jsonify(productos)


@app.route("/productos", methods=["POST"])
def registrar_producto():
    """
    Registra un nuevo producto en la lista.

    Parámetros:
        Recibe un JSON con id, nombre, precio y cantidad.

    Retorna:
        JSON: Producto registrado y mensaje de confirmación.
        Código 201: Registro exitoso.
        Código 400: Datos incorrectos o incompletos.
    """
    nuevo_producto = request.get_json(silent=True)

    if not isinstance(nuevo_producto, dict):
        return jsonify({
            "mensaje": "Debe enviar los datos del producto"
        }), 400

    if not all(campo in nuevo_producto for campo in ["id", "nombre", "precio", "cantidad"]):
        return jsonify({
            "mensaje": "Faltan datos del producto"
        }), 400

    productos.append(nuevo_producto)

    return jsonify({
        "mensaje": "Producto registrado correctamente",
        "producto": nuevo_producto
    }), 201


@app.route("/productos/<int:id_producto>", methods=["PUT"])
def actualizar_producto(id_producto):
    """
    Actualiza los datos de un producto registrado.

    Parámetros:
        id_producto (int): Identificador del producto.
        Recibe un JSON con los datos que se actualizarán.

    Retorna:
        JSON: Producto actualizado y mensaje de confirmación.
        Código 200: Actualización exitosa.
        Código 400: Datos incorrectos.
        Código 404: Producto no encontrado.
    """
    datos_actualizados = request.get_json(silent=True)

    if not isinstance(datos_actualizados, dict):
        return jsonify({
            "mensaje": "Debe enviar los datos del producto"
        }), 400

    for producto in productos:
        if producto["id"] == id_producto:
            producto["nombre"] = datos_actualizados.get("nombre", producto["nombre"])
            producto["precio"] = datos_actualizados.get("precio", producto["precio"])
            producto["cantidad"] = datos_actualizados.get("cantidad", producto["cantidad"])

            return jsonify({
                "mensaje": "Producto actualizado correctamente",
                "producto": producto
            }), 200

    return jsonify({
        "mensaje": "Producto no encontrado"
    }), 404


@app.route("/productos/<int:id_producto>", methods=["DELETE"])
def eliminar_producto(id_producto):
    """
    Elimina un producto de la lista mediante su ID.

    Parámetros:
        id_producto (int): Identificador del producto.

    Retorna:
        JSON: Mensaje de confirmación.
        Código 200: Eliminación exitosa.
        Código 404: Producto no encontrado.
    """
    for producto in productos:
        if producto["id"] == id_producto:
            productos.remove(producto)

            return jsonify({
                "mensaje": "Producto eliminado correctamente"
            }), 200

    return jsonify({
        "mensaje": "Producto no encontrado"
    }), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
