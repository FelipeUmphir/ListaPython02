#Início
A = float(input("Digite a 1ª valor:"))
B = float(input("Digite a 2ª valor:"))
C = float(input("Digite a 3ª valor:"))
D = float(input("Digite a 4ª valor:"))

if (D <= A):
    print(f"Os valores em ordem crescente são: {D}, {A}, {B}, e {C}")
else:
    if (D <= B):
        print(f"Os valores em ordem crescente são: {A}, {D}, {B}, e {C}")
    elif (D <= C):
        print(f"Os valores em ordem crescente são: {A}, {B}, {D}, e {C}")
    else:
        print(f"Os valores em ordem crescente são: {A}, {B}, {C}, e {D}")
#Fim