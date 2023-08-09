#Leia o valor de um produto,caso o valor seja menor do q 100 mostre a seguinte mensagem
#"VocÊ recebeu 5% de desconto", caso contrário
#"VocÊ recebeu 10% de desconto"
valor_prod = float(input("informe o valor do produto:"))
if valor_prod<100:
    print("VocÊ recebeu 5% de desconto")
else:
    print("VocÊ recebeu 10% de desconto")
    