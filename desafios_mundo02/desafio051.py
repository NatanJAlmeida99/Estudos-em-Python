# Desenvolva um programa que elia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
print("=" * 30)
print("10 TERMOS DE UMA PA".center(30))
print("=" * 30)

first = int(input("Primeiro termo: "))
jump = int(input("Razão: "))
decimo = first + (10 - 1) * jump

for c in range(first, decimo + jump, jump):
    print(c, end=" ⭢ ")
print("ACABOU")