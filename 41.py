#Início
N = 1
M = 0
print("As possibilidades da soma ser 7 são:")

while (N < 7):
    for i in range(1, 7):
        M = N + i
        if (M == 7):
            print(f"{N} + {i} = {M}")
    N = N + 1
#Fim