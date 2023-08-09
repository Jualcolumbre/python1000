valor1 = 45
valor2 = 258.45

#operadores aritiméticos
print("Soma", valor1+valor2)
print("Subtração", valor1-valor2)
print("Mutiplicação", valor1*valor2)
print("Divisão", valor1/valor2)
print(f"Divisão com duas casas decimais: {valor1/valor2:.2f}")
print(f"valor2: {valor2:.1f}")
#Obter dados do teclado(Entrada de dados)
usuario = input("informe o seu nome:")
print(f"Seja Bem-vindo(a) {usuario}")
#Conversão de tipo de dados - Casting
idade =int(input("Informe sua idade:"))
print(f"O nome do usuario é {usuario} e sua idade atual é {idade}")
#Mostrar o dobro da idade do usuario
print(f"O dobro da idade é: {idade*2}")
#Mostrar tipos de dados das variaveis
print("idade:",type(idade))
print("usuario",type(usuario))
valor_curso = float(input("Informe o valor pago pelo curso:"))
print(f"O valor informado foi {valor_curso}")
#Mostrar uma mensagem com 25% do valor do curso
#Parabéns!! VocÊ ganhou <valor> de crédito na próxima compra!!
print(f"Parabéns!! VocÊ ganhou R${valor_curso*25/100} de crédito na próxima compra!!")
#Solicitar quantidade de parcelas do pagamento
valor_parcelas = int(input("informe quantidade de parcelas:"))
#Mostrar valor das parcelas sem juros
print(f"Serão {valor_parcelas} de R${valor_curso/valor_parcelas} sem juros")