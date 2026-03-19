#Início
M = 0
N = int(input("Digite um número:"))

for i in range(1, N+1):
    M = M + 1 / i
print(f"O resultado da série é {M}")
#Fim