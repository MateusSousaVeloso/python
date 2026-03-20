print ("Sistema de Compras ByMaua")
valor_compra = float(input("Digite o valor da compra: "))
opcao_pagamento = int(input("Escolha: \n1 - Pagamento à vista \n2 - Pagamento à prazo\n--> "))
if opcao_pagamento == 1:
    forma_pagamento = int (input("Escolha: \n1 - PIX \n2 - Boleto\n--> "))
    if forma_pagamento == 1:
        desconto = valor_compra * 0.1
        valor_final = valor_compra * 0.9
        print("Parabéns, para pagamento a vista no pix, você tem:\nDesconto = %.2f e valor a pagar = %.2f" %(desconto,valor_final))
    elif forma_pagamento == 2:
        desconto = valor_compra * 0.05
        valor_final = valor_compra * 0.95
        print("Parabéns, para pagamento a vista no boleto, você tem:\nDesconto = %.2f e valor a pagar = %.2f" %(desconto,valor_final))
    else:
        print("Forma de pagamento inválida!!")
elif opcao_pagamento == 2:
    parcelas = int(input("Digite o número de parcelas (2 a 3): "))
    if parcelas == 2:
        valor_parcela = valor_compra / parcelas
        print("Valor de cada parcela: %.2f\nValor final: %.2f" %(valor_parcela, valor_compra))
    elif parcelas == 3:
        juros = valor_compra * 0.05
        valor_juros = valor_compra * 1.05
        valor_parcela = valor_juros / parcelas
        print("Valor de cada parcela: %.2f\nValor do juros: %.2f\nValor final: %.2f" %(valor_parcela, juros, valor_juros))
    else:
        print("Opção de parcelas inválida!!")
else:
    print("Opção de pagamento inválida!!")