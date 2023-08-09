#Listas compostas
pc = ['Processador', 'Mouse', 'Teclado',['memória Ram', 'HD', 'SSD'],'Webcam']
print("item 1:",pc[0])
print("item 4:",pc[3])
print("item4.1:",pc[3][0])
print("último item da sublista:",pc[3][-1])
# print(sorted(pc)) #nao funciona

pc[0]= "fonte"
print(pc)

#Substituir Mémoria ram por Mémoria flash
pc[3][0]= "Memória Flash"
print(pc)
