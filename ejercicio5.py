Calculadora básica: Escribe un programa que realice operaciones básicas (suma, resta, multiplicación y división) entre dos números introducidos por el usuario.


# Solicita al usuario que ingrese el primer número y lo convierte a un entero
num1 = int(input("Ingrese un número: "))

# Solicita al usuario que ingrese el segundo número y lo convierte a un entero
num2 = int(input("Ingrese un número: "))

# Imprime el menú de opciones para que el usuario elija la operación a realizar
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISIÓN")

# Solicita al usuario que ingrese la opción deseada y la convierte a un entero
op = int(input("Ingrese la opción a calcular: "))

# Inicia un bucle while que se ejecuta indefinidamente
while True:
   # Si la opción es 1, realiza la suma
   if op == 1:
      suma = num1 + num2
      print(suma)
      break # Sale del bucle
   # Si la opción es 2, realiza la resta
   elif op == 2:
      resta = num1 - num2
      print(resta)
      break # Sale del bucle
   # Si la opción es 3, realiza la multiplicación
   elif op == 3:
      multiplicacion = num1 * num2
      print(multiplicacion)
      break # Sale del bucle
   # Si la opción es 4, realiza la división
   elif op == 4:
      division = num1 / num2
      print(division)
      break # Sale del bucle
   # Si la opción no es válida, imprime un mensaje de error
   else:
      print("Número no válido")
      break # Sale del bucle