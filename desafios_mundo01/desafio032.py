# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date
year = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))

if year == 0:
    year = date.today().year
    if year % 4 == 0:
        print(f"O ano {year} é BISSEXTO")
    else:
        print(f"O ano {year} NÃO é BISSEXTO")

else:
    if year % 4 == 0 and year % 100 != 0:
        print(f"O ano {year} é BISSEXTO")
    else:
        print(f"O ano {year} NÃO é BISSEXTO")