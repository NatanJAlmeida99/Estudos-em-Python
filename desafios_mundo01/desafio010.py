# Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos Dólares ela pode comprar Considere US$1,00 = R$3,27
money = float(input("Quanto dinheiro você tem na carteira? R$"))
dollar = money / 3.27
print(f"Com R${money} você pode comprar US${dollar:.2f}")