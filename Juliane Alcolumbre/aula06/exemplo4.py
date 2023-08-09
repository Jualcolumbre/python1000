#Tuplas diferente da lista é imutável

cidades=('Manaus','Coari', 'Parintins','Manacapuru','Anori')
print(type(cidades))
#Mostrar o ultimo item da tupla
print(cidades[-1])
#Mostrar o primeiro item da tupla
print(cidades[0])
#Mostrar items ordenados
print(sorted(cidades))
#cidades.sort()
print(cidades)
# cidades[0] = 'Rio Preto Da Eva'
# print(cidades)
print(cidades.count ('Manaus'))

#Leia 3 números positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e o menor valor informado
num3 = []
for i in range(3):
    num3 = float(input("Informe um número:"))
    if 0>num3:
        print("DIGITE NÚMEROS POSITIVOS")
        continue
    else:
        print(num3)
        for i in num3:
            print(i, end=" ")
        print("Maior valor:",max(num3))
        print("Menor valor:",min(num3))
