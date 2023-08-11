from cgitb import text


try:
    txt = open("atividade final/dados_produtos.txt","a+")
    print("Arquivo encontrado")
    txt.seek(0)
    print(text.read())
except:
    print("Problemas ao abrir ....")








# try:
#     txt = open("Juliane Alcolumbre/atividade final/dados_produtos.txt","a+",encoding='utf-8')
#     prod = input("Digite o nome do produto:")
#     valor =float(input("Digite o valor do produto:"))
#     quant = int(input("Digite a quantidade de produto:"))
#     txt.write(f"-Produto:{prod}\n -Valor do Produto:{valor}\n -Quantidade:{quant}\n ")
# except:
#     print("Erro ao processar dados!!!")
# else:
#     txt.seek(0)
#     print(txt.read())
#     txt.close()
