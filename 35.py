#Início
z = 0
M = 0
x = int(input("Digite o 1º valor:"))
y = int(input("Digite o 2º valor:"))

if (x > y):
    z = x
    x = y
    y = z
    
for i in range(x+1, y):
    if (i % 2) != 0:
        M = M + i
print(f"O resultado da somatória dos números ímpares entre esses valores é {M}")
#Fim