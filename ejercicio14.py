# Pedimos al usuario que introduzca un número límite
numero_limite = int(input("Introduce un número límite: "))

# Inicializamos la variable sum a 0
sum = 0

# Creamos un bucle que itere desde 1 hasta el número límite
for i in range(1, numero_limite + 1):
    # En cada iteración, sumamos el valor de i a la variable sum
    sum += i

# Imprimimos el resultado
print("La suma de los números naturales hasta", numero_limite, "es:", sum)
     