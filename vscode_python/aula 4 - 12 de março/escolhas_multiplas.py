# ler um numero de 1 a 5 e exibi-lo por extenso

num = int(input("Digite um valor de 1 a 5: "))
if num == 1:
    print("um")
elif num == 2:
    print("dois")
elif num == 3:
    print("três")
elif num == 4:
    print("quatro")
elif num == 5:
    print("cinco")
else:
    print("Número inválido")

# Mesmo código utilizando match-case
