#Início
A = 0 
B = 1
C = 0
N = int(input("Digite um número:"))
print(f"A série de Fibonacci até o termo {N} é:")

for i in range(1, N+1):
    print(A)
    C = A
    A = B
    B = C + B
#Fim