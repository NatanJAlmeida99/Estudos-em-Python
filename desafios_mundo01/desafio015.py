# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado
days = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
tot_days = 60 * days
tot_km = km * 0.15
tot = tot_days + tot_km
print(f"O total a pagar é de R${tot:.2f}")