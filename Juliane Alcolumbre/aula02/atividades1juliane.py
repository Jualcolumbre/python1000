''''''
#1
print("Juliane Alcolumbre")
''''''
#2
nome = input("Digite seu nome:")
print("O seu nome é:",nome)
''''''
#3
nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
print(f"Seu nome é {nome} e sua idade é {idade}")
''''''
#4
numero = float(input("informe um número:"))
print(f"O dobro desse número é:{numero*2}")
print(f"A metade desse número é:{numero/2}")
''''''
#5
num1 = float(input("informe um número:"))
num2 = float(input("informe um número:"))
num3 = float(input("informe um número:"))
print("A soma total é:", num1+num2+num3)
''''''
#6
num1 = float(input("informe um número:"))
num2 = float(input("informe um número:"))
num3 = float(input("informe um número:"))
print(f"A mutiplicação entre {num1}, {num2}, {num3} é igual a:{num1*num2*num3}")
''''''
#7
num1 = float(input("informe a nota:"))
num2 = float(input("informe a nota:"))
num3 = float(input("informe a nota:"))
num4 = float(input("informe a nota:"))
soma = num1+num2+num3+num4
print("A média é:", soma/4)
''''''
#8
num1 = float(input("informe a medida em metros:"))
cm = int(num1*100)
print("A medida em centímetros é:",cm)
''''''
#9
num1 = float(input("informe um número:"))
cubo = float(num1*num1*num1)
quadrado = float(num1*num1)
print(f"O cubo do número é {cubo} e o quadrado {quadrado}")
''''''
#10
num1 = float(input("informe um número:"))
num2 = float(input("informe um número:"))
print("Total com casas decimais da divisão:",num1//num2)
print("Total sem casas decimais da divisão:",num1/num2)
'''
#11
'''
altura = float(input("Informe a altura do retÂngulo:"))
largura = float(input("Informe a largura do retÂngulo:"))
print("A área total em metros quadrados do retÂngulo é:", altura*largura)
'''
#12
'''
dias = int(input("Informe a quantidade de dias:"))
horas = int(input("Informe as horas:"))
minutos= int(input("Informe os minutos:"))
segundos= int(input("Informe os segundos:"))
tot_segs1= dias*24*60*60
tot_segs2= horas*60*60
tot_segs= minutos*60
print("O total se segundos é:",tot_segs1+tot_segs2+tot_segs+segundos)
'''
#13
'''
valor_prod = float(input("informe o valor do produto:"))
valor_c_desc= valor_prod*10/100
print("O valor do produto é:",valor_prod)
print("O valor do produto com desconto de 10% séra:",valor_prod-valor_c_desc)
print("O valor do desconto é:",valor_c_desc)
'''
#14
'''
n = float(input("Digite um número:"))
if n%2==0: 
    print("O valor informado é par")
else :    
    print("O valor informado é ímpar!")
'''
#15
'''
n = float(input("Digite o seu salário:"))
if n>1320:
    print("Seu salário é maior que o mínimo ")
elif n==1320:
    print("VocÊ recebe um salário mínimo")
else:
    print("VocÊ recebe mais que um salário mínimo")
''