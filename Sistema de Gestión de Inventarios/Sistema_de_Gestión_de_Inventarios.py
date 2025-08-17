# 1. Clase Producto
# Aquí definimos qué es un producto. Cada producto tiene un ID, un nombre, una cantidad y un precio.
# Los métodos "getters" nos ayudan a obtener los datos del producto y los "setters" nos permiten modificarlos.
class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.producto_id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        # Este método es útil para imprimir la información del producto de forma clara.
        return f"ID: {self.producto_id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# 2. Clase Inventario
# Esta clase actúa como el cerebro del sistema. Maneja la lista de todos los productos
# y tiene los métodos para añadir, eliminar, actualizar y buscar productos.
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Primero revisamos que el ID no exista para no tener productos duplicados.
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe. Por favor, elige uno diferente.")
            return False
        self.productos.append(producto)
        print("El producto se añadió correctamente.")
        return True

    def eliminar_producto(self, producto_id):
        # Borramos el producto si encontramos su ID.
        productos_antes = len(self.productos)
        self.productos = [p for p in self.productos if p.get_id() != producto_id]
        if len(self.productos) < productos_antes:
            print("El producto fue eliminado correctamente.")
            return True
        else:
            print("Error: No se encontró un producto con ese ID.")
            return False

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        # Encontramos el producto por su ID y actualizamos su cantidad o precio.
        for producto in self.productos:
            if producto.get_id() == producto_id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("El producto fue actualizado correctamente.")
                return True
        print("Error: No se encontró un producto con ese ID.")
        return False

    def buscar_por_nombre(self, nombre):
        # Buscamos productos que contengan el nombre que nos den, sin importar mayúsculas o minúsculas.
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        # Simplemente recorre la lista de productos e imprime la información de cada uno.
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for producto in self.productos:
                print(producto)
            print("-------------------------\n")


# 3. Interfaz de Usuario en la Consola
# Esta es la parte que el usuario ve y con la que interactúa. Aquí se muestra el menú
# y se llama a las funciones que definimos en la clase Inventario.
def main():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir un nuevo producto")
        print("2. Eliminar un producto")
        print("3. Actualizar la cantidad o el precio de un producto")
        print("4. Buscar productos por nombre")
        print("5. Ver todos los productos en el inventario")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            try:
                producto_id = input("ID del producto: ")
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                nuevo_producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Entrada inválida. Por favor, asegúrate de que la cantidad y el precio sean números.")

        elif opcion == '2':
            producto_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)

        elif opcion == '3':
            producto_id = input("ID del producto a actualizar: ")
            print("¿Qué quieres actualizar?")
            print("1. Cantidad")
            print("2. Precio")
            opcion_act = input("Elige una opción: ")

            try:
                if opcion_act == '1':
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    inventario.actualizar_producto(producto_id, nueva_cantidad=nueva_cantidad)
                elif opcion_act == '2':
                    nuevo_precio = float(input("Nuevo precio: "))
                    inventario.actualizar_producto(producto_id, nuevo_precio=nuevo_precio)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar un número.")

        elif opcion == '4':
            nombre_busqueda = input("Ingresa el nombre o parte del nombre que quieres buscar: ")
            resultados = inventario.buscar_por_nombre(nombre_busqueda)

            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for p in resultados:
                    print(p)
                print("----------------------------------\n")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")


if __name__ == "__main__":
    main()