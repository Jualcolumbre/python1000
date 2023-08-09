#Estrutura de repetição while (Continuação)
#Leia 5 números e mostre a soma de todos os valores informados
# c=1
# s=0 #Acumulador
# while c<=5:
#     n=float(input("Informe um valor:"))
#     s = s+n
#     c+=1
# print("Resultado da soma é:",s)
# print("="*50)

#Calcular a soma dos valores do intervalo(fechado) das variaves a e b (280)
# a=10
# b=25
# ab=0
# while a<=b:
#     print(a,end=" ")
#     ab+= a
#     a+=1
# print("\nO resultado é:",ab)
# print("="*50)
 
#Leia 2 valores e mostre a soma do intervalo entre eles
# t=int(input("Informe um valor:"))
# u=int(input("Informe um valor:"))
# tu=0
# if t<u:
#     while t<u:
#         print(t,end=" ")
#         tu+= t
#         t+=1
#     print("\nO resultado é:",tu)    
# elif u<t:   
#     while u<t:
#         print(u,end=" ")
#         tu+= u
#         u+=1    
#     print("\nO resultado é:",tu)
# else:
#     print("NÚMERO INVÁLIDO, DIGITE NOVAMENTE")
# print("="*50)

#Somar 5 valores positivos informados pelo úsuario
# s=0
# c=1
# while c<=5:
#     v=float(input("Informe um valor positivo:"))
#     if v<0:
#         continue
#     s += v
#     c+= 1
# print(f"O resultado da soma é {s}")

#Somar 5 valores negativos informados pelo úsuario
# s=0
# c=1
# while c<=5:
#     v=float(input("Informe um valor negativo:"))
#     if v>=0:
#        break
#     s+= v
#     c+= 1
# print(f"O resultado da soma é {s}")
 
#Leia 3 notas e mostre a média, caso seja digitado um valor negativo ou acima de 10 será solicitadoum novo valor
# s=0
# c=1
# while c<=3:
#     v=float(input("Informe a nota:"))
#     if v>10:
#        continue
#     elif v<0:
#         continue
#     s+= v
#     c+= 1
# print(f"O resultado da média é {s/3}")