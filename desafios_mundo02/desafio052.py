# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input("Digite um número: "))
count = 0

for c in range(1, num + 1):
    if (num % c == 0):
        count += 1
if (count != 2):
    print(f"O número {num} foi divisível {count} vezes")
    print("E por isso ele NÃO É UM PRIMO!")
else:
    print(f"O número {num} foi divisível {count} vezes")
    print("E por isso ele é PRIMO!")