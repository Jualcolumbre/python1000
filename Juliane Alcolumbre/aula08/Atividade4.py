# 1.Crie uma função em Python para retornar a área de um retângulo, considere a seguinte fórmula: h=a*l
def a_retangulo(a,l):
    return (a*l)
print(a_retangulo(10,4))
# 2.Crie uma função em Python para mostrar a área de um círculo, considere a seguinte fórmula: A=3,14*r**2
def a_circulo(r):
    area = 3.14*r*r
    return  area
print(a_circulo(7))
# 3.Crie uma função em Python para mostrar o produto da multiplicação entre n valores.
def valores(lista):
    resultado=lista[0]
    for i in lista:
        resultado=resultado*i
    return resultado
 
lista = [1,5,2,6,3]
print(valores(lista))
# 4.Crie uma função em Python para mostrar apenas as chaves de um dicionário.
def chaves(dici):
    return dici.keys()
dici = {111:"Karla da Silva",222:"Hélio Santos",333:"Manoel Gomes",444:"Bruna Mattos"}
print(chaves(dici))
        
 
# 5.Crie uma função em Python para mostrar apenas os valores de um dicionário.
def chaves(dici):
    return dici.values()

dici = {111:"Karla da Silva",222:"Hélio Santos",333:"Manoel Gomes",444:"Bruna Mattos"}
print(chaves(dici))
# 6.Crie uma função em Python para mostrar as chaves e os valores de um dicionário.
def chaves(dici):
    return dici.items()

dici = {111:"Karla da Silva",222:"Hélio Santos",333:"Manoel Gomes",444:"Bruna Mattos"}
print(chaves(dici))
# 7.Crie uma função em Python para retornar a quantidade de itens existentes em um dicionário.
def qtd_itens(dici):
    return dici.len()

dici = {111:"Karla da Silva",222:"Hélio Santos",333:"Manoel Gomes",444:"Bruna Mattos"}
print(qtd_itens(dici))