import math  # Importa el módulo math que contiene constantes y funciones matemáticas

# Solicita al usuario que ingrese el radio del círculo y lo convierte a un entero
radio = int(input("Ingrese el radio del círculo: "))

# Calcula el área del círculo usando la fórmula área = π * radio^2
area = (math.pi) * (radio**2)

# Imprime el resultado del cálculo del área
print("Esta es su área: ", area)