
# Pedimos al usuario que introduzca un número
numero_usuario = int(input("Introduce un número: "))

# Inicializamos la variable factorial a 1
factorial = 1

# Creamos un bucle que itere desde 1 hasta el número introducido
for i in range(1, numero_usuario + 1):
    # En cada iteración, multiplicamos el valor de i por la variable factorial
    factorial *= i

# Imprimimos el resultado
print("El factorial de", numero_usuario, "es:", factorial)