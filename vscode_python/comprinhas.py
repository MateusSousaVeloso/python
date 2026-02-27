# ler: nome do produto, valor unitário e quantidade comprada
# calcular o total da compra
# se a quantidade for maior que 100, definir um desconto de 10%
# exibir saída adequada

nome_produto = input("Digite o nome do produto comprado: ")
valor_produto = float(input("Digite o valor de 1 (Uma) unidade do produto: "))
qtd_produto = int(input("Digite a quantidade de unidades do produto a serem compradas: "))

valor_total = valor_produto * qtd_produto
if qtd_produto > 100:
    valor_descontado = valor_total * 0.9
    print("Por ter comprado mais de 100 produtos, você recebeu um desconto de 10%")
    print("O valor total saiu de %.2f para valor final %.2f" %(valor_total,valor_descontado))
else:
    print("O valor total é de: %.2f"  %valor_total)