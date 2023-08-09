#Aula de listas

lista = [2,8,10,4,55,'coxinha',34,'maionese',33]
print(type(lista))
print('Primeiro item da lista:',lista[0])
print('Último item da lista:',lista[8])
print('Último item da lista:',lista[-1])
print('Penultimo item da lista:',lista[-2])
print('Quantidade de itens ds lista:',len(lista))

#Lista Ordenada
pc = ['Mouse', 'Monitor', 'HD', 'Memória Ram', 'CÂmera']
print(sorted(pc))
lista2 = [6,8,4,11,55,0,3]
print(sorted(lista2))

#Mostrar intervalos da lista
print(lista2)
print(lista[2:5])
print(lista2[3:])
print(lista2[:4])

#Inserir item ao final da lista
lista2.append(1000)
print(lista2)

#Inserir item em determinada posição 
lista2.insert(2,5000)
print(lista2)

#Unir duas listas
lista2.extend(lista)
print(lista2)

#Remover último item da lista ou o índice informado
lista2.pop(0)
print(lista2)

#Remover item específico da lista
lista2.remove('coxinha')
print(lista2)

#Copiar referÊncia
lista3 = pc
#Copiar objeto
lista4 = pc.copy()
print("Lista 3",lista3)
print("Lista 4",lista4)
pc.append("SSD")
pc.append("Teclado")
print(lista3)
lista3.append("Placa de vídeo")
print(lista4)
print(pc)
