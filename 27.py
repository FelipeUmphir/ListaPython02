#Início
n = int(input("Digite o número de voltas:"))
d = float(input("Digite a extensão do circuito, em metros:"))
t = float(input("Digite o tempo de duração, em minutos:"))

V = (d / t) * n
Vm = (V * 3.6)
print(f"A velocidade média é de {Vm} km/h")
#Fim