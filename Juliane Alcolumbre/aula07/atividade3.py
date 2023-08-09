#1.	Crie um dicionário contendo os nomes dos estados abreviados (Chave) e os nomes das capitais (Valor) da região norte e nordeste.
#  Mostre ao final as informações relacionadas ao amazonas e Sergipe.
''''''
# Estados={'AM':'Manaus','AC':'Rio Branco','PE':'Recife','BA':'Salvador','SE':'Aracajú','PI':'Terezina','PA':'Belém','TO':'Palmas'}
# print(Estados['AM'],Estados['SE'])
''''''
#2.	Crie um script que leia o nome de 5 alunos e mostre os dados informados em ordem alfabética
''''''
# alunos = []
# for i in range(5):
#     num = input("Informe o nome do aluno:")
#     alunos.append(num)
# print(sorted(alunos))
''''''
#3.	Crie uma lista com os seguintes valores: 
# [2,10,30,85,2,6,0,4]
#  	- Mostre apenas o terceiro valor
# 	- Mostre apenas o último valor
# - Mostre o dobro de cada valor
''''''
# lista=[2,10,30,85,2,6,0,4]
# print(lista[2])
# print(lista[-1])
# lista2 = [i*2 for i in lista]
# print(lista2)
''''''
#4.	Qual a principal diferença entre uma lista e uma tupla em Python?
''''''
# print("A tupla é imutável e a lista não")
''''''
#5.	Pesquise e responda quais a principais características da Estrutura Set em Python.
''''''
# print("Os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados.")
# print("Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.")
# ''''''
#6.	Descreva quatro exemplos de funções/métodos que podem ser aplicados em um dicionário.
''''''
# print("keys: Mostra somente as chaves do dicionário","\n value:Mostrar somente os valores armazenados no dicionário","\n items:Mostrar todos os itens do dicionário","\n update:Atualizar dicionário")
# ''''''
#7.	Crie um script que leia dez números positivos e armazene os dados em uma lista, 
# mostre os dados em ordem crescente, o maior valor informado e menor valor informado.
''''''
# lista4=[]
# for i in range(10):
#     num = float(input("Informe um número:"))
#     if num>0:
#         lista4.append(num)
# print(lista4)
# print("Lista ordenada:",sorted(lista4))
# print("Maior valor:",max(lista4))
# print("Menor valor:",min(lista4))
# ''''''