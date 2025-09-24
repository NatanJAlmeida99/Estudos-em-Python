salary = float(input("Qual é o salário do funcionário? R$ "))

if salary > 1250:
    aumento = salary * 0.10
    new_salary = salary + aumento
else:
    aumento = salary * 0.15
    new_salary = salary + aumento

print(f"Quem ganhava R${salary:.2f} passa a ganhar R${new_salary:.2f} agora")