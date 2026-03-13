peso_pacote = float(input("Diga o peso do pacote a ser enviado: "))

if peso_pacote <= 0:
    print("Peso inválido")
elif peso_pacote <= 1:
    print("Frete leve")
elif peso_pacote <= 5:
    print("Frete normal")
elif peso_pacote <= 10:
    print("Frete pesado")
else: 
    print("Frete especial")