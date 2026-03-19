#Início
T = int(input("Digite o tipo de investimento:"))
V = float(input("Digite o valor investimento:"))

if (T == 1):
    VC = (V * 1.03)
    print(f"O valor corrigido é {VC} reais")
elif (T == 2):
    VC = (V * 1.05)
    print(f"O valor corrigido é {VC} reais")
else:
    print("Tipo de investimento inválido")
#Fim