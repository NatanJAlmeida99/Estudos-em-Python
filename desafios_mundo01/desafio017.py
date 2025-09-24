# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
cateto1 = float(input("Comprimento do cateto oposto: "))
cateto2 = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(cateto1, cateto2)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")