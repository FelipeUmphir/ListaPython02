#Início
A = float(input("Digite a 1ª nota:"))
B = float(input("Digite a 2ª nota:"))
C = float(input("Digite a 3ª nota:"))
D = float(input("Digite a 4ª nota:"))
M = (A + B + C + D) / 4
print(f"A média do aluno foi {M}")

if (M >= 6):
    print("Status: Aprovado")
elif (M >= 3):
    print("Status: Exame")
else:
    print("Status: Retido")
#Fim