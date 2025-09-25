# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são de maiores

from datetime import date

count_maior = 0
count_menor = 0

for c in range(1, 8):
    year = date.today().year
    year_born = int(input(f"Em que ano a {c}° pessoa nasceu? "))
    age = year - year_born
    if (age >= 18):
        count_maior += 1
    else:
        count_menor += 1

print(f"Ao todo tivemos {count_maior} maiores de idade")
print(f"E também tivemos {count_menor} pessoas menores de idade")