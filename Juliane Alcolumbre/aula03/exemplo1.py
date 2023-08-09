#Estruturas de decisão (Condicionais)
'''
Leia a idade do aluno e defina sua categoria de acordo com seguintes informações:
Categoria - idade
Sem categoria - Menor do que 3
Infantil - 3 ate 10 anos
Juvenil - 11 ate 17 
Adulto - 18 ate 39
Senior - 40 ate 130
Acima de 130 idade invalida
'''

idade = int(input("Informe a Idade do aluno:"))
if idade<3:
    print("Sem Categoria!")
elif idade<=10:
    print("Aluno da categoria: Infantil!")
elif idade<=17:
    print("Aluno da categoria: Juvenil!")
elif idade<=39:
    print("Aluno da categoria: Adulto!")
elif idade<=130:
    print("Aluno da categoria: SÊnior!")
else:
    print("Idade Inválida!!")

