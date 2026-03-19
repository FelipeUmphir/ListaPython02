#Início
M = 0

for i in range(1, 16):
    if (i % 2) == 0:
        M = M - i/(i ** 2)
    else:
        M = M + i/(i ** 2)
print(f"O resultado da série é {M}")
#Fim