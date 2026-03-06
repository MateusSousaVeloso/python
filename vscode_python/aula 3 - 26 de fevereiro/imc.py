#Ana está criando um sistema para calcular o indice de Massa Corporal (IMC) e fornecer recomendações básicas. 0 programa deve receber o peso e a altura den uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule ○ IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18,5 <= IMC < 25) ou acima do peso (IMC >= 25).

#ENTRADAS
altura = float(input('Forneça sua altura em metros: '))
peso = float(input('Forneça seu peso em kilogramas: '))

#PROCESSAMENTO
imc = peso / (altura * altura)
imc_arredondado = round(imc, 2)

#SAÍDA
print('\nSeu IMC é:', imc_arredondado)
if imc_arredondado < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc_arredondado < 25:
    print('Você está no peso ideal.')
else:
    print('Você está acima do peso.')