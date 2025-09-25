# Desenvolva um programa que leia seis números interios e mostre a soma apneas daqueles que foram pares. Se o valor digitando for ímpar, desconsidere-o

soma = 0
count = 0

for c in range(1, 7):
    num = int(input(f"Digite o {c}° valor: "))
    if num % 2 == 0:
        soma += num
        count += 1
print(f"Você informou {count} números PARES e a soma foi {soma}")