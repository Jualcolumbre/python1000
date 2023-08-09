#Primeiro script em Python
print("hello, world!!!")
print('Curso Programando com Python')
print('-'*20)
print("Carga horária:40h \n10 dias")
#padrão snake case
nome_pessoa= "Juliane Alcolumbre"
nome_curso= "Programando com Python"
idade = 21
valor_curso = 250.99
#mostrar tipos de dados das variaveis
print(type(nome_pessoa))
print(type(idade))
print(type(valor_curso))
#concatenar dados
print("Seja Bem-vindo(a)",nome_pessoa)
print("Seja Bem-vindo(o)", nome_pessoa, "ao curso", nome_curso)
#o curso <nome_curso> custa <valor>
print("O curso", nome_curso, "custa R$", valor_curso )
#f-strings no python
print(f"Seja Bem-vindo {nome_pessoa}")
print(f"O curso {nome_curso} custa R$ {valor_curso}")