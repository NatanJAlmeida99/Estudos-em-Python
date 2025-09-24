# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas

km = int(input("Qual é a distância da sua viagem? "))

if km <= 200:
    expense = km * 0.50
    print(f"Você está prestes a começar uma viagem de {km:.1f}Km.\nE o preço da sua passagem será de R${expense:.2f}")
else:
    expense = km * 0.45
    print(f"Você está prestes a começar uma viagem de {km:.1f}Km.\nE o preço da sua passagem será de R${expense:.2f}")