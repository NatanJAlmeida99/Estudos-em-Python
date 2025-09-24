# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salary =  float(input("Qual é o salário do Funcionário? R$"))
aumento = salary * 0.15
new_salary = salary + aumento
print(f"Um funcionário que ganaha R${salary}, com 15% de aumento, passa a receber R${new_salary:.2f}")