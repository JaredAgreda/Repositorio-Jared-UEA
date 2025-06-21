class Animal:
    """Clase base para todos los animales."""
    def hacer_sonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):  # Perro hereda de Animal
    """Clase para perros."""
    def hacer_sonido(self):  # Sobrescribe el método del padre
        print("¡Guau!")

class Gato(Animal):  # Gato hereda de Animal
    """Clase para gatos."""
    def hacer_sonido(self):  # Sobrescribe el método del padre
        print("¡Miau!")

# --- Uso del programa (Polimorfismo) ---
# Creamos una lista con objetos de diferentes clases (pero con un ancestro común).
animales = [Perro(), Gato()]

# Llamamos al mismo método en cada objeto, y cada uno responde de forma diferente.
for animal in animales:
    animal.hacer_sonido()