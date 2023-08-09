#Trabalhar com estrutura de dados dicionário(dict)

dados ={}
print(type(dados))
#Estrutura chave e valor(dicionário)
alunos= {111:"Karla da Silva",222:"Hélio Santos",333:"Manoel Gomes",444:"Bruna Mattos"}
#Mostrar o primeiro item do dicionário
print(alunos[111])
#Mostrar somente as chaves do dicionário
print(alunos.keys())
#Mostrar somente osz valores armazenados no dicionário
print(alunos.values())
#Mostrar todos os itens do dicionário
print(alunos.items())
#Atualizar dicionário
alunos.update({555:"Paulo Coelho"})
print(alunos)
alunos[666]= 'teste'
print(alunos)
alunos[111]= 'Carlos da Silva'
print(alunos)
#Excluir um item do dicionário
alunos.pop(666)
print(alunos)
#Mostrar sonente os valores do dicionário
for i in  alunos.values():
    print(i)
#Mostrar somente as chaves do dicionário
for i in  alunos.keys():
    print(i)
#mostrar todos os itens de um dicionário
for i in  alunos.items():
    print(i)

for i,j in  alunos.items():
    print(i,"-",j)

for i,j in  alunos.items():
    print(i,j,sep="-")

dados = {
    'lista_a':[1,2,2,5,8],
    'lista_b':[10,20,30,40],
    'lista_c':[100,200,300,400]
}
print(dados)
print(type(dados))
#Mostrar o último item da lista b
print("útimo item:",dados['lista_b'][-1])
 