from abc import ABC, abstractmethod

# 1. Clase Abstracta (La idea o "contrato")
# Define lo que un vehículo DEBE poder hacer, pero no cómo.
class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        # Cada vehículo se moverá a su manera.
        pass

# 2. Clases Concretas (Las implementaciones reales)
# Ahora decimos CÓMO se mueve cada tipo de vehículo.
class Coche(Vehiculo):
    def mover(self):
        print("El coche acelera en la carretera.")

class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta avanza pedaleando.")

# 3. Uso del programa
# Creamos objetos de nuestras clases concretas.
mi_coche = Coche()
mi_bici = Bicicleta()


vehiculos = [mi_coche, mi_bici]

for vehiculo in vehiculos:
    vehiculo.mover()