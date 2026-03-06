import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Isso não é uma equação do segundo grau (a deve ser diferente de 0).")
else:
    delta = (b ** 2) - 4 * a * c
    if delta < 0:
        parte_real = (-b) / (2 * a)
        parte_imaginaria = (math.sqrt(abs(delta))) / (2 * a)
        print("\nDelta menor que 0")
        if parte_real == 0:
            print(f"Raíz imaginária: ±{parte_imaginaria:g}i")
        else:
            print(f"Raízes imaginárias: {parte_imaginaria:g}i + {parte_real:g} e {parte_imaginaria:g}i - {parte_real:g}")
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print("\nDelta igual a 0")
        print(f"Raiz única: {raiz:g}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("\nDelta maior que 0")
        if abs(raiz1) == abs(raiz2): 
            print(f"Raiz: ±{abs(raiz1):g}")
        else: 
            print(f"Raiz 1: {raiz1:g} e Raiz 2: {raiz2:g}")