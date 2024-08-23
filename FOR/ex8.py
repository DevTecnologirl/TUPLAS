lista = [5, 8, 12, 20, 33]
numero_procurado = 12
encontrado = False
for numero in lista:
    if numero == numero_procurado:
        encontrado = True
        break
if encontrado:
    print(f"O número {numero_procurado} foi encontrado na lista.")
else:
    print(f"O número {numero_procurado} não foi encontrado na lista.")
