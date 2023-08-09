#Leia dois números inteiros e mostre somente o menor valor
num1 = int(input("informe um número:"))
num2 = int(input("informe um número:"))
if num1>num2:
    print(f"O número {num2} é o menor valor!!")
elif num1==num2:
    print("VocÊ digitou números iguais!")
else:
    print(f"O número {num1} é o menor valor!!")

