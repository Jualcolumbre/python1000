#Ler nome e email e armazenar no arquivos dados3.txt

try:
    txt = open("Juliane Alcolumbre/aula09/dados3.txt","a+",encoding='utf-8')
    nome = input("Informe o nome:")
    email = input("Informe o e-mail:")
    txt.write(f"{nome:>2}\n - {email:>5}\n")
except:
    print("Erro ao gravar os dados!!!")