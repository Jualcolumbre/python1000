#Abertura de um arquivo chamado dados2.txt

from os import write


try:
    txt = open ("Juliane Alcolumbre/aula09/dados2.txt","w+")
    for i in range(10):
        nome = input("Informe um nome:")
        txt.write(f"Nome:{nome}\n")
except:
    print("Não foi possível encontrar o arquivo")
else:
    txt.close()

#ou ler 10 nomes de outro jeito
try:
    txt = open ("Juliane Alcolumbre/aula09/dados2.txt","a+")
    for i in range(1,11):
        nome = input("Informe um nome:")
        txt.write(f"{i} - Nome:{nome}\n")
except:
    print("Não foi possível encontrar o arquivo")
else:
    txt.seek(0)
    print(txt.read())
    txt.close()