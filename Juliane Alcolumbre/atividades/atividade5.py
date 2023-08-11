# Crie uma função que leia o nome e as notas de um aluno e salve em um arquivo o nome, a média e data do registro.
# Crie uma função que leia o nome do curso, carga horária e valor e registre em um arquivo.
# Crie uma função mostre todos os dados cursos registrados na questão anterior.
# Pesquise funções/métodos para apagar um arquivo e aplique um exemplo.

try:
    txt = open("Juliane Alcolumbre/dados5.txt","a+",encoding='utf-8')
    nome = input("Informe o nome do Aluno(a):")
    txt.write (f"{nome}")
except:
     print("Erro ao gravar os dados!!!")
else:
    txt.close()     