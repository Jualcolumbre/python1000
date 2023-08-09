#Criar uma lista de  notas
notas = [6.25,2,10,9,8.8]

#Valor máximo de uma nota na lista
print("Maior valor:",max(notas))

#Valor mínimo de uma nota na lista
print("Menor valor:",min(notas))

#Quantidade de itens na lista de notas
print("Quantidade de notas:",len(notas))

#Soma total das notas da lista
print("Soma das notas:",sum(notas))

#Mostrar média das notas na lista
print(f"Média aritmética:{sum(notas)/len(notas):.2f}")

#Operador in
print(10 in notas)

#Loop for com listas
print(notas)
for i in notas:
    print(i, end=" ")

#Leia 5 notas utilizando listas e estruturas de repetição
print("\n")
notas2 = []
for i in range(5):
    num = float(input("Informe a nota:"))
    notas.append(num)

print("Todas as notas informadas:", notas2)
print("A quantidade de notas:", len(notas2))
print("A soma das notas é:", sum(notas2))

#Leia uma quantidade de notas determida pelo usuário e faça a soma dos valores digitados
qtd = int(input("Informe a quantidade de notas:"))
cont = 0
notas3 = []
#Adicionar somente valores de 0 a 10
while cont<=qtd:
    num=float(input("Informe a nota:"))
    if num>=0 and num<=10:
        notas.append(num)
    else:
        continue
    cont +=1
print("Total é:",sum(notas3))

