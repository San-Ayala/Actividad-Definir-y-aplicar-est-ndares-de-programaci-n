
import { useState } from "react"

function Productos() {

    const [productos, setProductos] = useState([])
    const [id, setId] = useState("")
    const [nombre, setNombre] = useState("")
    const [precio, setPrecio] = useState("")
    const [cantidad, setCantidad] = useState("")

    async function consultarProductos() {
        let respuesta = await fetch("http://127.0.0.1:5000/productos")
        let datos = await respuesta.json()
        setProductos(datos)
    }

    async function registrarProducto() {
        if (id === "" || nombre === "" || precio === "" || cantidad === "") {
            alert("Complete todos los campos")
            return
        }

        let respuesta = await fetch("http://127.0.0.1:5000/productos", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id: Number(id),
                nombre: nombre,
                precio: Number(precio),
                cantidad: Number(cantidad)
            })
        })

        let datos = await respuesta.json()
        alert(datos.mensaje)

        if (respuesta.ok) {
            consultarProductos()
        }
    }

    async function actualizarProducto() {
        if (id === "") {
            alert("Ingrese el ID del producto")
            return
        }

        let respuesta = await fetch("http://127.0.0.1:5000/productos/" + id, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nombre: nombre,
                precio: Number(precio),
                cantidad: Number(cantidad)
            })
        })

        let datos = await respuesta.json()
        alert(datos.mensaje)

        if (respuesta.ok) {
            consultarProductos()
        }
    }

    async function eliminarProducto() {
        if (id === "") {
            alert("Ingrese el ID del producto")
            return
        }

        let respuesta = await fetch("http://127.0.0.1:5000/productos/" + id, {
            method: "DELETE"
        })

        let datos = await respuesta.json()
        alert(datos.mensaje)

        if (respuesta.ok) {
            consultarProductos()
        }
    }

    return (
        <div>
            <h1>API TIENDA</h1>

            <h2>Gestionar productos</h2>

            <input
                type="number"
                placeholder="ID"
                value={id}
                onChange={(e) => setId(e.target.value)}
            />

            <input
                type="text"
                placeholder="Nombre"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
            />

            <input
                type="number"
                placeholder="Precio"
                value={precio}
                onChange={(e) => setPrecio(e.target.value)}
            />

            <input
                type="number"
                placeholder="Cantidad"
                value={cantidad}
                onChange={(e) => setCantidad(e.target.value)}
            />

            <div>
                <button onClick={registrarProducto}>
                    Registrar producto
                </button>

                <button onClick={actualizarProducto}>
                    Actualizar producto
                </button>

                <button onClick={eliminarProducto}>
                    Eliminar producto
                </button>
            </div>

            <h2>Lista de productos</h2>

            <button onClick={consultarProductos}>
                Consultar productos
            </button>

            <table border="1">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Precio</th>
                        <th>Cantidad</th>
                    </tr>
                </thead>

                <tbody>
                    {productos.map((producto) => (
                        <tr key={producto.id}>
                            <td>{producto.id}</td>
                            <td>{producto.nombre}</td>
                            <td>{producto.precio}</td>
                            <td>{producto.cantidad}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Productos
