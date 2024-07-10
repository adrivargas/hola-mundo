Par o Impar: Escribe un programa que determine si un número introducido por el usuario es par o impar.


# Solicita al usuario que ingrese un número y lo convierte a un entero
num1 = int(input("Ingrese un número: "))

# Verifica si el número ingresado es par
if num1 % 2 == 0:
  # Si el número es par, imprime el mensaje correspondiente
  print("El número es par")
else:
  # Si el número es impar, imprime el mensaje correspondiente
  print("El número es impar")
