# Solicita al usuario que introduzca una cadena
cadena = input("Ingrese una cadena: ")

# Normaliza la cadena eliminando espacios y convirtiendo a minúsculas
cadena_normalizada = cadena.replace(" ", "").lower()

# Verifica si la cadena normalizada es igual a su versión invertida
es_palindromo = cadena_normalizada == cadena_normalizada[::-1]

# Muestra el resultado
if es_palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")