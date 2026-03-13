n1 = int(input("Diga o primeiro numero: "))
n2 = int(input("Diga um segundo numero: "))

operacao = int(input("Escolha:\n1 - Soma\n2 - Subtração\n3 - Multplicação\n"))

if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 - n2
elif operacao == 3:
    resultado = n1 * n2

if operacao != 1 | 2 | 3:
    print("Operação inválida")
else: 
    print(f"O resultado é {resultado}")