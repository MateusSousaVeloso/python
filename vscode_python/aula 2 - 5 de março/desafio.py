a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print("\nDesafio 1")
if a > b:
    print("A é maior")
else:
    print("B é maior")

print("\nDesafio 2")
if a > b:
    print("A é maior")
elif b > a:
    print("B é maior")
else:
    print("Os números são iguais")

print("\nDesafio 3")
print(f"O maior número é {max(a, b, c)}")
