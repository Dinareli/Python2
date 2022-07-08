menor = maior = 0

for n in range(10):
    idade = int(input("Digite a sua idade:\n"))

    if idade <= 17:
        menor = menor + 1
    else:
        maior = maior + 1

print("Menores de idade: ", menor)
print("Maior: ", maior)
