# Faça um algoritmo que elia o preço de um produto e mostre seu novo preço, com 5% de desconto
price = float(input("Qual é o preço do produto? R$ "))
desc = price * 0.05
new_price = price - desc
print(f"O produto que custava R${price}, na promoção com desconto de 5% vai custar R${new_price:.2f}")