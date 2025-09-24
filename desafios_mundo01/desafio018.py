# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseo e tangente desse ângulo
import math
angulo = int(input("Digite o ângulo que você deseja: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {sen:.2f}\nO ângulo de {angulo} tem o COSSENO de {cos:.2f}\nO ângulo de {angulo} tem o TANGETE de {tan:.2f}")