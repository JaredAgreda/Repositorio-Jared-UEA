import os

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
        """Obtiene el ID único del producto."""
        return self.producto_id

    def get_nombre(self):
        """Obtiene el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Obtiene la cantidad actual del producto en inventario."""
        return self.cantidad

    def get_precio(self):
        """Obtiene el precio del producto."""
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        """Establece una nueva cantidad para el producto."""
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        """Establece un nuevo precio para el producto."""
        self.precio = nuevo_precio

    def __str__(self):
        # Este método es útil para imprimir la información del producto de forma clara y legible.
        return f"ID: {self.producto_id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_csv_line(self):
        """Convierte los atributos del producto en una línea CSV para almacenamiento."""
        return f"{self.producto_id},{self.nombre},{self.cantidad},{self.precio}"

# 2. Clase Inventario
# Esta clase actúa como el cerebro del sistema. Maneja la colección de todos los productos
# y tiene los métodos para añadir, eliminar, actualizar y buscar productos.
class Inventario:
    def __init__(self, archivo_nombre="inventario.txt"):
        # Usamos un diccionario 'self.productos' para almacenar los objetos Producto.
        # La CLAVE del diccionario será el ID del producto (string) y el VALOR será el objeto Producto.
        # Esto permite una búsqueda, adición y eliminación de productos muy eficiente (en tiempo constante promedio, O(1)),
        # ya que accedemos directamente por su ID único.
        self.productos = {}  # Cambiado de lista a diccionario para un acceso más eficiente por ID
        self.archivo_nombre = archivo_nombre
        # Al crear el objeto Inventario, intentamos cargar los datos desde el archivo.
        self.cargar_inventario()

    def guardar_inventario(self):
        """
        Guarda el estado actual del inventario (todos los productos en el diccionario)
        en un archivo de texto. Cada producto se serializa a una línea CSV simple.
        """
        try:
            with open(self.archivo_nombre, "w") as archivo:
                # Iteramos sobre los VALORES del diccionario, que son los objetos Producto.
                for producto in self.productos.values():
                    linea = producto.to_csv_line() + "\n"
                    archivo.write(linea)
            print("Inventario guardado correctamente en el archivo.")
        except IOError:
            print(f"Error: No se pudo escribir en el archivo '{self.archivo_nombre}'.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al guardar el archivo: {e}")

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo de texto al iniciar el programa.
        Deserializa cada línea CSV, crea un objeto Producto y lo añade al diccionario
        'self.productos' usando su ID como clave.
        """
        # Limpiamos el inventario actual antes de cargar para evitar duplicados si se llama varias veces.
        self.productos = {}
        try:
            if not os.path.exists(self.archivo_nombre):
                print(f"Archivo de inventario '{self.archivo_nombre}' no encontrado. Se creará uno nuevo al guardar.")
                # Creamos el archivo vacío si no existe para evitar errores posteriores.
                with open(self.archivo_nombre, "w"):
                    pass
                return

            with open(self.archivo_nombre, "r") as archivo:
                for linea in archivo:
                    # Leemos cada línea, la dividimos por comas y creamos un objeto Producto.
                    partes = linea.strip().split(',')
                    if len(partes) == 4:
                        producto_id, nombre, cantidad_str, precio_str = partes
                        try:
                            cantidad = int(cantidad_str)
                            precio = float(precio_str)
                            producto = Producto(producto_id, nombre, cantidad, precio)
                            # Añadimos el producto al diccionario, usando su ID como CLAVE.
                            self.productos[producto_id] = producto
                        except ValueError:
                            print(f"Advertencia: Saltando línea con formato incorrecto en el archivo: {linea}")
                    else:
                        print(f"Advertencia: Saltando línea con un número incorrecto de partes: {linea.strip()}")
            print("Inventario cargado exitosamente desde el archivo.")
        except FileNotFoundError: # Este bloque ahora es redundante debido a la comprobación inicial
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
        except IOError:
            print(f"Error: No se pudo leer el archivo '{self.archivo_nombre}'. Revisa los permisos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al cargar el archivo: {e}")

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Utiliza el diccionario para verificar rápidamente si el ID ya existe.
        """
        if producto.get_id() in self.productos:  # Verificación eficiente en el diccionario (O(1))
            print("Error: El ID del producto ya existe. Por favor, elige uno diferente.")
            return False
        # Si el ID no existe, añadimos el producto al diccionario.
        self.productos[producto.get_id()] = producto
        self.guardar_inventario()
        print(f"Producto '{producto.get_nombre()}' añadido correctamente.")
        return True

    def eliminar_producto(self, producto_id):
        """
        Elimina un producto del inventario por su ID.
        Utiliza el diccionario para una eliminación eficiente.
        """
        if producto_id in self.productos:  # Verificación eficiente en el diccionario (O(1))
            nombre_producto_eliminado = self.productos[producto_id].get_nombre()
            del self.productos[producto_id]  # Eliminación eficiente del diccionario (O(1))
            self.guardar_inventario()
            print(f"El producto '{nombre_producto_eliminado}' (ID: {producto_id}) fue eliminado correctamente.")
            return True
        else:
            print(f"Error: No se encontró un producto con el ID '{producto_id}'.")
            return False

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto existente.
        Accede al producto directamente a través de su ID en el diccionario.
        """
        if producto_id in self.productos:  # Acceso eficiente en el diccionario (O(1))
            producto = self.productos[producto_id]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            self.guardar_inventario()
            print(f"El producto '{producto.get_nombre()}' (ID: {producto_id}) fue actualizado correctamente.")
            return True
        print(f"Error: No se encontró un producto con el ID '{producto_id}'.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre (no distingue entre mayúsculas y minúsculas).
        Itera sobre los valores del diccionario para encontrar coincidencias.
        Retorna una lista de objetos Producto que coinciden.
        """
        resultados = []
        # Iteramos sobre los VALORES del diccionario (los objetos Producto) para buscar por nombre.
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        """
        Muestra todos los productos actualmente en el inventario.
        Ordena los productos por su ID para una presentación consistente.
        """
        if not self.productos:  # Comprobamos si el diccionario está vacío
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            # Para mostrar, podemos obtener los productos ordenados por su ID para una mejor legibilidad.
            # Iteramos sobre las claves ordenadas y luego accedemos al producto en el diccionario.
            for producto_id in sorted(self.productos.keys()):
                print(self.productos[producto_id])
            print("-------------------------\n")


# 3. Interfaz de Usuario en la Consola
# Esta es la parte que el usuario ve y con la que interactúa. Aquí se muestra el menú
# y se llama a las funciones que definimos en la clase Inventario.
def main():
    # Al iniciar, se carga el inventario automáticamente desde el archivo.
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
            producto_id = input("ID del producto (único): ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                if cantidad < 0 or precio < 0:
                    print("La cantidad y el precio no pueden ser negativos. Inténtalo de nuevo.")
                    continue
                nuevo_producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Entrada inválida. Por favor, asegúrate de que la cantidad y el precio sean números válidos.")

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
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa. Inténtalo de nuevo.")
                        continue
                    inventario.actualizar_producto(producto_id, nueva_cantidad=nueva_cantidad)
                elif opcion_act == '2':
                    nuevo_precio = float(input("Nuevo precio: "))
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo. Inténtalo de nuevo.")
                        continue
                    inventario.actualizar_producto(producto_id, nuevo_precio=nuevo_precio)
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar un número válido.")

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
