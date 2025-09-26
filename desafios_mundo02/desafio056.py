# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#   A média de idade do grupo
#   Qual é o nome do homem mais velho
#   Qunatas mulheres têm menos de 20 anos

age_tot = 0
old_man = ""
maior_age_man = 0
count_woman = 0

for person in range(1, 5):
    print("-" * 5, f"{person}° PESSOA", "-" * 5)
    name = str(input("Nome: "))
    age = int(input("Idade: "))
    sex = str(input("Sexo [M/F]: ")).upper()
    age_tot += age

    if person == 1:
        maior_age_man = age
        old_man = name
    if sex in "M" and age > maior_age_man:
        maior_age_man = age
        old_man = name

    if sex == "F" and age < 20:
        count_woman += 1

med_age = age_tot / 4

print(f"A média de idade do grupo é de {med_age} anos")
print(f"O homem mais velho tem {maior_age_man} anos e se chama {old_man}")
print(f"Ao todo são {count_woman} mulheres com menos de 20 anos")
