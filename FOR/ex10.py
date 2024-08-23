numeros = [-4, -2, -1, 0, 1, 2, 3, 4, 5]

# Listas para armazenar números positivos e negativos
positivos = []
negativos = []

# Variável para verificar se todos os números são positivos
todos_positivos = True

# Iterando sobre a lista de números
for numero in numeros:
    if numero > 0:
        positivos.append(numero)  # Adiciona à lista de positivos
    elif numero < 0:
        negativos.append(numero)  # Adiciona à lista de negativos
        todos_positivos = False  # Define como False se encontrar um número negativo

# Exibindo os resultados
if todos_positivos:
    print("Todos os números são positivos.")
else:
    print("Nem todos os números são positivos.")

print("Números positivos:", positivos)
print("Números negativos:", negativos)
