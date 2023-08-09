#Estruturs de repetição While
cont = 0 
while cont <=100:
    print(cont,end=" ")
    cont = cont+1
print("\nValor final do contador:", cont)  
#Contagem iniciando em 50 até 200
cont = 50
while cont <=200:
    print(cont,end=" ")
    cont += 1
print("\nValor final do contador:", cont)  
print("="*20)
#Contagem iniciando em 10 e finalizando em 80, incrementando os valores de 10 em 10
cont = 10
while cont <=80:
    print(cont,end=" ")
    cont += 10
print("\nValor final do contador:", cont)  
#Mostrar mensagem "eu tenho que estudar" 300x
i = 1
while i <= 300 :
    print(i,"- Eu tenho que estudar")
    i += 1 
#Leia um número e mostre a contagem a partir do 0 até o número informado
j = int(input("Digite um número maior q 0:"))
i = 0
while i <= j:
    print(i,end=" ")
    i+=1
print("\n","-"*20)
#Contagem decrescente iniciando em 23 até 0
l = 23
while l>= 0:
    print(l, end=" ")
    l -=1
print("\n","-"*20)
#Leia 2 números e mostre a contagem do intervalo dos valores informados
t = int(input("Digite o valor inicial:"))
f = int(input("Digite o valor final:"))
if t<f:
    while t<=f:
     print(t, end=" ")
     t +=1
else:
    while f<=t:
        print(f, end=" ")
        f +=1

