#Aplicar operadores lógicos com if
#Leia a quantidade de faltas de um aluno e sua média final
faltas = int(input("Informe a quntidade de faltas:"))
media = float(input("Informe a média final:"))
#Condições de reprovação
#Quantidade de faltas maior que 8 ou média menor que 7
print("-"*50)
#analisar condições do aluno somente se o valor das faltas for maior ou igual a zero
if faltas<0:
    print("Valor de faltas inválido!")
else:       
    if faltas>8 or media<7:
        print("Aluno Reprovado")
        if faltas>8 and media<7:
            print("Aluno reprovou por faltas e por media não atingida")
        elif media<7:
            print("Aluno reprovou por não atingir a média")
        else :
            print("Aluno reprovou por faltas")
    else:       
        print("Aluno Aprovado")
