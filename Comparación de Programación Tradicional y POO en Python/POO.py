# La 'Clase' es la plantilla para crear nuestros objetos de clima.
class ClimaSemanal:
    # El constructor se ejecuta al crear un objeto. Aquí preparamos los datos.
    def __init__(self):
        self._temperaturas = []  # El objeto guardará las temperaturas aquí

    # Método para ingresar las temperaturas y guardarlas DENTRO del objeto.
    def ingresar_temperaturas(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        print("--- Ingreso de Temperaturas (POO) ---")
        for dia in dias:
            while True:
                try:
                    temp = float(input(f"Temperatura del {dia}: "))
                    self._temperaturas.append(temp)
                    break  # Sale del bucle si el número es válido
                except ValueError:
                    print("Error: Ingrese un valor numérico.")

    # Método para calcular el promedio usando los datos del propio objeto.
    def calcular_promedio(self):
        total = sum(self._temperaturas)
        return total / len(self._temperaturas)

# --- Programa Principal ---
# 1. Creamos un objeto (una instancia) a partir de nuestra clase.
reporte_clima = ClimaSemanal()

# 2. Le pedimos al objeto que ejecute sus métodos.
reporte_clima.ingresar_temperaturas()
promedio = reporte_clima.calcular_promedio()

# 3. Mostramos el resultado.
print(f"\nEl promedio de temperatura de la semana es: {promedio:.2f}°C")