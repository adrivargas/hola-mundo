#Número mayor: Escribe un programa que pida tres números al usuario y determine cuál es el mayor.


# Creamos una lista vacía para almacenar los números ingresados por el usuario
numeros = []

# Solicitamos al usuario que ingrese tres números
for i in range(3):
    num = int(input(f"Ingrese número {i+1}: "))  # Pedimos al usuario que ingrese un número
    numeros.append(num)  # Añadimos el número a la lista

# Determinamos el número mayor utilizando la función max()
mayor = max(numeros)

# Imprimimos el número mayor
print("El número mayor es:", mayor)
