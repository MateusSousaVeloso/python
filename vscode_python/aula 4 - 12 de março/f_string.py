# Caso simples
nome = "Bia"
idade = 18
print(f"{nome} tem {idade} anos.")
a = 3
b = 7
print(f"{a} + {b} = {a + b} ")

# Acrecentando formatos: {valor:formato}
pi = 3.14159265
print(f"pi = {pi:.3f}") # .3f faz sair apenas 3 casas decimais

#  Numero de casas ocupadas
n = 42
m = 126
p = 34567
print(f"m = {m:8}")
print(f"n = {n:8}")
print(f"p = {p:8}")

#  Alinhamento de texto
texto = "batata"
print(f"| {texto:<12} |") #Texto na esquerda
print(f"| {texto:>12} |") #Texto na direita
print(f"| {texto:^12} |") #Texto no centro

frase = "O rato roeu a roupa do rei de Roma"
print(f"| {frase:^12} |") # O limite é ignorado

#  Preenchimento de caracter
n = 3
print(f"n = {n:05}")

# Formatação para %
juros = 0.65789
print(f"taxa = {juros:.2%}")

# Separador de milhar
numero = 2345678909
print(f"{numero:,}")