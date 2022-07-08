for x in range(5):
    numero = int(input("Digite um número: "))

    if x == 0:
        menorNumero = numero

if numero < menorNumero:
     menorNumero = numero
print("O menor número digitado é", menorNumero)