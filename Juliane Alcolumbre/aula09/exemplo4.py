#Mostrar exeções ao dirigir números negativos

n = float(input("Informe um valor positivo:"))
if n<0:
    raise ValueError("Númro negativo =(")
    