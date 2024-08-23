n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

while n > 1:
    fatorial *= n
    n -= 1

print(f"O fatorial é {fatorial}.")
#n!=n×(n−1)×(n−2)