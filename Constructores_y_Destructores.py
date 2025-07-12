# --- Definición de la Clase ---
class Recurso:
    # El constructor se ejecuta al crear un objeto: Recurso("Mi Recurso")
    # Su función es inicializar los datos del objeto.
    def __init__(self, nombre):
        self.nombre = nombre
        print(f" Recurso '{self.nombre}' creado. (Constructor __init__ llamado)")

    # El destructor se ejecuta cuando el objeto va a ser eliminado.
    # Su función es realizar tareas de limpieza (ej. cerrar un archivo).
    def __del__(self):
        print(f" Recurso '{self.nombre}' liberado. (Destructor __del__ llamado)")

# --- Demostración ---
print("Iniciando programa...")

# 1. Creamos una instancia. Esto llama al constructor __init__.
print("Creando objeto 'mi_recurso'...")
mi_recurso = Recurso("Temporal")

# 2. Eliminamos la instancia. Esto llama al destructor __del__.
print("Eliminando objeto 'mi_recurso'...")
del mi_recurso

print("Programa finalizado.")