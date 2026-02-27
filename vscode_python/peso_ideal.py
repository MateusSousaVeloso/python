# Ler o sexo (masculino ou feminino) e a altura de uma pessoa em metros. Calcular o peso ideal : 
# masculino: pi = 72.7 x altura - 58 
# feminino: p1 = 62.1 x altura - 44.7
sexo = input('Diga seu sexo: ')
altura = float(input('Diga sua altura em metros: '))

if sexo == "masculino":
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1 * altura - 44.7
print("Seu peso ideal sendo do sexo %s é: %.2f" %(sexo, peso_ideal))