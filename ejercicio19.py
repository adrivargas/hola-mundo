# Pedimos al usuario que introduzca su peso en kilogramos
peso_usuario = float(input("Introduce tu peso en kilogramos: "))

# Pedimos al usuario que introduzca su altura en metros
altura_usuario = float(input("Introduce tu altura en metros: "))

# Calculamos el IMC utilizando la fórmula: IMC = peso / altura^2
imc = peso_usuario / (altura_usuario ** 2)

# Redondeamos el IMC a dos decimales
imc_redondeado = round(imc, 2)

# Imprimimos el resultado
print("Tu índice de masa corporal (IMC) es:", imc_redondeado)

# Clasificamos el IMC según la categoría correspondiente
if imc_redondeado < 18.5:
    print("Tu categoría es: Bajo peso")
elif imc_redondeado < 25:
    print("Tu categoría es: Peso normal")
elif imc_redondeado < 30:
    print("Tu categoría es: Sobrepeso")
else:
    print("Tu categoría es: Obesidad")
     