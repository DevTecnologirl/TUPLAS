numero = int(input("Digite um número para ver sua tabuada: "))
contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1