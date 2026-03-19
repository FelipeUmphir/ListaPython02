#Início
x = int(input("Digite o 1º valor:"))
y = int(input("Digite o 2º valor:"))
z = 0

if (x > y):
    z = x
    x = y
    y = z

print("Os números primos exitentes entre esses valores são:")
for n in range(x + 1, y):

    p = True

    for i in range(2, n):
        if (n % i) == 0:
            p = False
            break

    if (p == True):
        print(n)
#Fim