# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto; à vista no cartão: 5% de desconto; em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros
print("=" * 11, end=" ")
print("LOJAS GUANABARA", "=" * 11)
price = float(input("Preço das compras: R$ "))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
option = int(input("Qual é a opção: "))

if (option == 1):
    percentage = price * 0.10
    price_end = price - percentage
    print(f"Sua compra de R${price:.2f} vai custar R${price_end:.2f} no final")
elif (option == 2):
    percentage = price * 0.05
    price_end = price - percentage
    print(f"Sua compra de R${price:.2f} vai custar R${price_end:.2f} no final")
elif (option == 3):
    valor_parcelado = price / 2      
    print(f"Sua compra de R${price:.2f} será parceladas em 2x de R${valor_parcelado:.2f} SEM JUROS")
elif (option == 4):
    parcelas = int(input("Quantas parcelas? "))
    percentage = price * 0.20
    price_end = price + percentage
    value_parcelado = price_end / parcelas
    print(f"Sua comprar será parcelada em {parcelas}x de R${value_parcelado:.2f} COM JUROS")
    print(f"Sua compra de R${price:.2f} vai custar R${price_end:.2f} no final")
else:
    print("Opção inválida")