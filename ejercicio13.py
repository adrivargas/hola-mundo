# Definimos una función que determina si un número es primo
def es_primo(n):
    # Si el número es menor o igual a 1, no es primo
    if n <= 1:
        return False

    # Iteramos desde 2 hasta la raíz cuadrada de n (inclusive)
    for i in range(2, int(n ** 0.5) + 1):
        # Verificamos si n es divisible entre i
        if n % i == 0:
            # Si es divisible, no es primo
            return False

    # Si no encontramos ningún divisor, es primo
    return True

# Pedimos al usuario que introduzca un número
numero_usuario = int(input("Introduce un número: "))

# Verificamos si el número es primo utilizando la función es_primo()
if es_primo(numero_usuario):
    # Si es primo, imprimimos un mensaje
    print("El número", numero_usuario, "es primo.")
else:
    # Si no es primo, imprimimos otro mensaje
    print("El número", numero_usuario, "no es primo.")