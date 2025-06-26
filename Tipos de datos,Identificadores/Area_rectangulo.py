# Programa que calcula el área de un rectángulo y muestra el resultado.

# Definición de variables con diferentes tipos de datos
nombre_figura = "Rectángulo"     # string
largo_figura = 10                # integer
ancho_figura = 5.5               # float
mostrar_resultado = True         # boolean

# Cálculo del área
area_calculada = largo_figura * ancho_figura

# Mostrar la información en pantalla
print(f"Figura: {nombre_figura}")

if mostrar_resultado:
    print(f"Largo: {largo_figura}")
    print(f"Ancho: {ancho_figura}")
    print(f"Área: {area_calculada}")