# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço. Se é a hora de se alistar. Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
year = date.today().year
user_year = int(input("Ano de nascimento: "))
age = year - user_year

if age < 18:
    alist = 18 - age
    print(f"Quem nasceu em {user_year} tem {age} em {year}\nAinda falta {alist} anos para o alistamento\nSeu alistamento será em {year + alist}")
elif age == 18:
    print(f"Quem nasceu em {user_year} tem {age} anos em {year}\nVocê tem que se alistar IMEDIATAMENTE")
else:
    alist = age - 18
    print(f"Quem nasceu em {user_year} tem {age} anos em {year}.\nVocê já deveria ter se alistado há {alist} anos\nSeu alistamento foi em {year - alist}")