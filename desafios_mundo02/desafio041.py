# A Confederação Nacional precisa de um programa que leia o ano de nascimento de um atleta e motre sua categoria de acordo com a idade: Até 9 anos: MIRIM, Até 14: INFANTIL, Até 19 anos: JUNIOR, Até 20 anos: SÊNIOR, ACIMA: Master
from datetime import date
year = date.today().year
user_year = int(input("Ano de Nascimento: "))
age = year - user_year
print(f"O atleta tem {age} anos")

if (age < 9):
    print("Classificação: MIRIM")
elif(age < 14):
    print("Classificação: INFANTIL")
elif(age < 19):
    print("Classificação: JUNIOR")
elif(age <= 20):
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")