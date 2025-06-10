# Pide las 7 temperaturas y las devuelve en una lista.
def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print("--- Ingreso de Temperaturas (Tradicional) ---")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp)
                break  # Sale del bucle si el número es válido
            except ValueError:
                print("Error: Ingrese un valor numérico.")
    return temperaturas

# Recibe una lista de temperaturas y calcula su promedio.
def calcular_promedio(lista_temps):
    total = sum(lista_temps)
    return total / len(lista_temps)

# --- Programa Principal ---
# 1. Llamamos a una función para obtener los datos.
temperaturas_semanales = ingresar_temperaturas()

# 2. Pasamos esos datos a otra función para que los procese.
promedio_semanal = calcular_promedio(temperaturas_semanales)

# 3. Mostramos el resultado.
print(f"\nEl promedio de temperatura de la semana es: {promedio_semanal:.2f}°C")