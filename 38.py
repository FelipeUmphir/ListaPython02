#Início
N = 0
Me = 0
Ma = 0

while (N < 100):
    X = int(input("Digite um valor:"))
    if (X > Ma):
        Ma = X
    if (X < Me):
        Me = X
    elif (Me == 0):
        Me = X
    N = N + 1
print(f"O maior valor digitado é {Ma} e o menor é {Me}")
#Fim