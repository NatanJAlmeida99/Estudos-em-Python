# Faça um programa que elia uma frase pelo teclado e mostre: Quantas vezs aparece a letra "A" / Em que posição ela aparece a primeira vez / Em que posição ela aparece a última vez
phase = str(input("Digite uma frase: ").upper().strip())
count_a = phase.count("A")
find_a = phase.find("A")
last_a = phase.rfind("A")
print(f"A letra A aparece {count_a} vezes na frase")
print(f"A primeira letra A apareceu na posição {find_a + 1}")
print(f"A última letra A apareceu na posição {last_a + 1}")