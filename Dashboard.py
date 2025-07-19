import os
import sys  # Importamos sys para usar la ruta del intérprete de Python actual


# --- Personalización de la Interfaz con Colores (Opcional) ---
# Usamos secuencias de escape ANSI para dar color a la salida en la terminal.
class Colores:
    HEADER = '\033[95m'  # Morado claro
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    ADVERTENCIA = '\033[93m'  # Amarillo
    ERROR = '\033[91m'  # Rojo
    RESET = '\033[0m'  # Resetear al color por defecto
    NEGRITA = '\033[1m'


# --- Funciones Auxiliares ---

def limpiar_pantalla():
    """Limpia la pantalla de la consola para una mejor visualización."""
    # os.name es 'nt' para Windows, y 'posix' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo de script.
    Se ha mejorado la presentación visual con colores.
    """
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n{Colores.HEADER}--- Código de {os.path.basename(ruta_script)} ---{Colores.RESET}\n")
            print(Colores.AZUL + archivo.read() + Colores.RESET)
            input(f"\n{Colores.ADVERTENCIA}Presiona Enter para continuar...{Colores.RESET}")
    except FileNotFoundError:
        print(f"{Colores.ERROR}El archivo no se encontró.{Colores.RESET}")
    except Exception as e:
        print(f"{Colores.ERROR}Ocurrió un error al leer el archivo: {e}{Colores.RESET}")


# --- Nueva Funcionalidad: Ejecutar Script ---

def ejecutar_script(ruta_script):
    """
    Ejecuta el script de Python seleccionado en una nueva instancia.
    """
    print(f"\n{Colores.VERDE}--- Ejecutando {os.path.basename(ruta_script)} ---{Colores.RESET}\n")
    # Usamos sys.executable para asegurarnos de que se ejecuta con el mismo intérprete de Python
    # que está corriendo este dashboard. Las comillas dobles aseguran que funcione con rutas con espacios.
    os.system(f'"{sys.executable}" "{ruta_script}"')
    print(f"\n{Colores.VERDE}--- Ejecución finalizada ---{Colores.RESET}")
    input(f"\n{Colores.ADVERTENCIA}Presiona Enter para continuar...{Colores.RESET}")


# --- Menús Interactivos ---

def gestionar_acciones_script(ruta_script, descripcion):
    """
    Muestra un submenú para un script específico, permitiendo ver su código o ejecutarlo.
    """
    while True:
        limpiar_pantalla()
        print(f"{Colores.HEADER}Acciones para: {Colores.NEGRITA}{descripcion}{Colores.RESET}")
        print("1 - Ver código")
        print("2 - Ejecutar script")
        print("0 - Volver al menú principal")

        eleccion = input("\nElige una acción: ")

        if eleccion == '1':
            mostrar_codigo(ruta_script)
            break  # Vuelve al menú principal después de la acción
        elif eleccion == '2':
            ejecutar_script(ruta_script)
            break  # Vuelve al menú principal después de la acción
        elif eleccion == '0':
            break  # Sale de este submenú y vuelve al principal
        else:
            print(f"{Colores.ERROR}Opción no válida. Intenta de nuevo.{Colores.RESET}")
            input("Presiona Enter para continuar...")


def mostrar_menu_principal():
    """
    Función principal que muestra el dashboard y gestiona la selección del usuario.
    """
    # Define la ruta base donde se encuentra este script (dashboard.py)
    ruta_base = os.path.dirname(__file__)

    # --- ¡Personaliza tus scripts aquí! ---
    # La nueva estructura permite una descripción amigable y la ruta relativa.
    # Así, el menú es más limpio para el usuario.
    opciones = {
        '1': {
            'descripcion': 'Ejemplo de Técnicas de Programación',
            'ruta': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py'
        },
        '2': {
            'descripcion': 'Calculadora Simple (Ejemplo)',
            'ruta': 'proyectos/calculadora.py'  # Asegúrate de que esta ruta y archivo existan
        },
        '3': {
            'descripcion': 'Generador de Saludos (Ejemplo)',
            'ruta': 'proyectos/saludos.py'  # O cualquier otra ruta que necesites
        }
    }

    while True:
        limpiar_pantalla()
        print(f"{Colores.HEADER}{Colores.NEGRITA}---  DASHBOARD DE PROYECTOS PYTHON  ---{Colores.RESET}")

        # Imprime las opciones del menú de forma más amigable
        for key, value in opciones.items():
            print(f"{Colores.AZUL}{key}{Colores.RESET} - {value['descripcion']}")

        print(f"\n{Colores.ADVERTENCIA}0 - Salir del Dashboard{Colores.RESET}")

        eleccion = input("\nElige un script o '0' para salir: ")

        if eleccion == '0':
            print(f"\n{Colores.VERDE}¡Hasta luego! {Colores.RESET}")
            break
        elif eleccion in opciones:
            # Construye la ruta absoluta del script seleccionado
            info_script = opciones[eleccion]
            ruta_relativa = info_script['ruta']
            descripcion = info_script['descripcion']
            ruta_script_absoluta = os.path.join(ruta_base, ruta_relativa)

            # Llama al submenú de acciones para el script elegido
            gestionar_acciones_script(ruta_script_absoluta, descripcion)
        else:
            print(f"\n{Colores.ERROR}Opción no válida. Por favor, intenta de nuevo.{Colores.RESET}")
            input("Presiona Enter para continuar...")


# --- Punto de Entrada Principal ---
# Se asegura de que el código se ejecute solo cuando el archivo es el principal.
if __name__ == "__main__":
    mostrar_menu_principal()
