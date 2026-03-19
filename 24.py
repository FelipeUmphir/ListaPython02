#Início
x = int(input("Digite um valor:"))
x1 = (x % 2)
x2 = (x % 3)

if (x1 == 0):
    print("É divisível por 2")
else:
    print("Não é divisível por 2")

if (x2 == 0):
    print("É divisível por 3")
else:
    print("Não é divisível por 3")
#Fim