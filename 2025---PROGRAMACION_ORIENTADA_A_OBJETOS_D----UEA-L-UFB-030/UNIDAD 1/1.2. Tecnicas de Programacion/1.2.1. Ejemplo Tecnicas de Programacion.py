import random  # Necesario para el ataque especial aleatorio de Saiyan


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        # Cálculo de daño base, puede ser sobrescrito por clases hijas
        return max(0, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        daño_causado = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño_causado
        print(self.nombre, "ha realizado", int(daño_causado), "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", int(enemigo.vida))
        else:
            enemigo.morir()


class Saiyan(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, poder_ki):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.poder_ki = poder_ki  # Multiplicador de daño específico para Saiyans

    def atributos(self):
        super().atributos()
        print("·Poder Ki:", self.poder_ki)

    def daño(self, enemigo):
        # Daño potenciado por la fuerza y el poder Ki
        return max(0, (self.fuerza * self.poder_ki) - enemigo.defensa)

    def super_ataque_ki(self, enemigo):
        # Ataque especial con mayor daño
        daño_especial = max(0,
                            (self.fuerza * self.poder_ki * 1.5) - enemigo.defensa)  # Factor de 1.5 para el super ataque
        print(f"{self.nombre} lanza un SUPER ATAQUE KI!")
        enemigo.vida = enemigo.vida - daño_especial
        print(self.nombre, "ha realizado", int(daño_especial), "puntos de daño especial a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", int(enemigo.vida))
        else:
            enemigo.morir()

    def atacar(self, enemigo):
        # Los Saiyans tienen una probabilidad de usar su ataque especial
        if random.random() < 0.25:  # 25% de probabilidad
            self.super_ataque_ki(enemigo)
        else:
            # Llama al método atacar de la clase Personaje, pero se usará el
            # método daño() sobrescrito por Saiyan si es llamado desde una instancia de Saiyan
            super().atacar(enemigo)


def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        if jugador_1.esta_vivo():
            print(f"\n>>> Acción de {jugador_1.nombre}:")
            jugador_1.atacar(jugador_2)

        if not jugador_2.esta_vivo(): break  # Termina si el jugador 2 muere

        if jugador_2.esta_vivo():
            print(f"\n>>> Acción de {jugador_2.nombre}:")
            jugador_2.atacar(jugador_1)

        turno += 1

    print("\n========== FIN DEL COMBATE ==========")
    if jugador_1.esta_vivo() and not jugador_2.esta_vivo():
        print(f"¡Ha ganado {jugador_1.nombre}!")
    elif jugador_2.esta_vivo() and not jugador_1.esta_vivo():
        print(f"¡Ha ganado {jugador_2.nombre}!")
    else:  # Ambos no están vivos o alguna otra condición de empate
        print("¡Es un EMPATE!")


# Creación de Goku y Vegeta
goku = Saiyan(nombre="Goku", fuerza=22, inteligencia=8, defensa=15, vida=250, poder_ki=5)
vegeta = Saiyan(nombre="Vegeta", fuerza=21, inteligencia=10, defensa=14, vida=240, poder_ki=5)

print("--- ATRIBUTOS INICIALES ---")
goku.atributos()
vegeta.atributos()

print("\n\n--- COMBATE: GOKU VS VEGETA ---")

combate(goku, vegeta)