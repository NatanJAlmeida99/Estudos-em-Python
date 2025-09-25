from time import sleep
from random import randint
itens = ("Pedra", "Papel", "Tesoura")
print("-=" * 10)
print("""Suas opções?
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
print("-=" * 10)

user = int(input("Qual é a sua jogada: "))
pc = randint(0, 2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=" * 10)
print(f"Computador jogou {itens[pc]}")
print(f"Jogador jogou {itens[user]}")
print("-=" * 10)

if (user == 0):
    if (pc == 0):
        print("EMPATO")
    elif (pc == 1):
        print("COMPUTADOR VENCE")
    elif (pc == 2):
         print("JOGADOR VENCE")
elif (user == 1):
    if (pc == 0):
        print("JOGADOR VENCE")
    elif (pc == 1):
        print("EMPATO")
    elif (pc == 2):
        print("COMPUTADOR VENCE")
elif (user == 2):
    if (pc == 0):
        print("COMPUTADOR VENCE")
    elif (pc == 1):
        print("JOGADOR VENCE")
    elif (pc == 2):
        print("EMPATO")
else:
    print("Opção inválida")