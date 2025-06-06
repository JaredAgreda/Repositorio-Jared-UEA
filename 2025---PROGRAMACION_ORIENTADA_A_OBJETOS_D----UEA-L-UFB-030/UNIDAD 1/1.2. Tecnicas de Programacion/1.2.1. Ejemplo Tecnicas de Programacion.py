# Clase base (Abstracción)
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Encapsulamiento (atributo privado)
        self.__modelo = modelo

    # Método para obtener la información del vehículo
    def mostrar_info(self):
        return f"Vehículo: {self.__marca} {self.__modelo}"

    # Método abstracto (simulando abstracción)
    def arrancar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


# Clase derivada (Herencia)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Herencia (usando el constructor de la clase base)
        self.__puertas = puertas  # Encapsulamiento

    # Polimorfismo (sobrescribiendo el método arrancar)
    def arrancar(self):
        return f"{self.mostrar_info()} está arrancando con {self.__puertas} puertas."

    # Método adicional para mostrar detalles específicos del auto
    def mostrar_detalles(self):
        return f"{self.mostrar_info()} tiene {self.__puertas} puertas."


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto de la clase Auto
    mi_auto = Auto("Toyota", "Corolla", 4)

    # Mostrar información usando polimorfismo
    print(mi_auto.arrancar())  # Salida: Vehículo: Toyota Corolla está arrancando con 4 puertas.

    # Mostrar detalles específicos del auto
    print(mi_auto.mostrar_detalles())  # Salida: Vehículo: Toyota Corolla tiene 4 puertas.