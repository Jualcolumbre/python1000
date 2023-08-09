#Leia a idade do usuário e informe se ele é maioe ou menor de idade
#Verificar números negativos antes da idade
idade = int(input("Informe sua idade:"))

if idade<0:
    print("Idade inválida")
    print("Verifique o valor informado!")
else:
    if idade>=18:
        print("VocÊ é maior de idade!!")
    else: 
       print("VocÊ é menor de idade!!")