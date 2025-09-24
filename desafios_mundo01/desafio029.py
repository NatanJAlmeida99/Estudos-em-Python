# Escreva um programa que elia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre um mesangem dizendo que ele foi multado. A multa vai custa R$7,00 por cada KM acima do limete
speed = int(input("Qual é a velocidade atual do carro? "))

if speed <= 80:
    print("Tenha um bom dia! Dirigia com segurança!")
else:
    print("MULTADO! Você excedeu o limete permitido que é de 80km/h")
    penalty = speed - 80
    value = penalty * 7
    print(f"Você deve pagar uma multa de R${value:.2f}!")