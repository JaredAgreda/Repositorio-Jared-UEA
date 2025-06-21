class CuentaBancaria:
    """Modelo simple de una cuenta bancaria."""

    # El constructor inicializa los datos.
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado para proteger el saldo.

    # Método para ingresar dinero.
    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Depósito de ${cantidad}. Saldo actual: ${self.__saldo}")

    # Método para sacar dinero.
    def retirar(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            print(f"Retiro de ${cantidad}. Saldo actual: ${self.__saldo}")
        else:
            print("Fondos insuficientes.")


# --- Uso del programa ---
mi_cuenta = CuentaBancaria("Juan Pérez", 100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(30)