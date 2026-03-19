#Início
M = 1
O = 1
N = int(input("Digite um número:"))

for i in range(1, N+1):
    O = O * i
    M = M + 1/O
print(f"O resultado da série é {M}")
#Fim