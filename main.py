import math,os

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

os.system("clear")
som = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
pote = math.pow(n1,n2)
raizn1 = math.sqrt(n1)
raizn2 = math.sqrt(n2)

print("Soma: ",som)
print("Subtração: ",sub)
print("Multiplicação: ",mult)
print("Divisão: ",div)
print("Potenciação: ",pote)
print("Raiz: ",raizn1)
print("Raiz: ",raizn2)


