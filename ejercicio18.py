
import random

# Genera 5 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(5)]

# Muestra los números aleatorios generados
print("Números aleatorios generados:")
for numero in numeros_aleatorios:
    print(numero)
