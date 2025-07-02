# 1. Clase Base y Encapsulación
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = 0  # Atributo encapsulado para proteger su acceso

    # Método que será sobrescrito (Polimorfismo)
    def describir(self):
        return f"Vehículo {self.marca} {self.modelo}"

# 2. Clase Derivada (Herencia)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase padre
        self.puertas = puertas

    # 3. Polimorfismo: se sobrescribe el método de la clase padre
    def describir(self):
        return f"Coche {self.marca} {self.modelo} con {self.puertas} puertas."

# --- Demostración ---
# Se crean instancias (objetos)
vehiculo_generico = Vehiculo("Toyota", "Genérico")
mi_coche = Coche("Ford", "Focus", 4)

# Se demuestra el polimorfismo: el mismo método `describir()` actúa diferente
print(vehiculo_generico.describir())
print(mi_coche.describir())

# Se demuestra la herencia: 'mi_coche' usa un atributo de 'Vehiculo'
mi_coche._velocidad = 120
print(f"Velocidad del coche: {mi_coche._velocidad} km/h")