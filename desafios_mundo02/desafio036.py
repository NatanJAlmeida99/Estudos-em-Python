# Escreva um program para aprovar o empr´stimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimos será negado

house = float(input("Valor da casa: R$"))
salary = float(input("Salário do comprador: R$"))
years = int(input("Quantos anos de financiamento: "))

prestacao = house / (years * 12)
minino = salary * 0.30

if prestacao < minino:
    print(f"Para pagar uma casa de R${house:.2f} em {years} anos a prestação será de R${prestacao:.2f}")
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print(f"Para pagar uma casa de R${house:.2f} em {years} anos a prestação será de R${prestacao:.2f}")
    print("Empréstimo NEGADO!")