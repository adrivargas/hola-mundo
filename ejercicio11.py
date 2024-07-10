# Pedimos al usuario que ingrese el número a multiplicar
num1 = int(input("Ingrese el número a multiplicar: "))

# Mostramos la tabla de multiplicar
print("Tabla de multiplicar del", num1)
for i in range(1, 11):
    multiplicacion = num1 * i
    print(f"{num1} x {i} = {multiplicacion}")
