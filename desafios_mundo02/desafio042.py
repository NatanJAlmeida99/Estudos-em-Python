# Refaça o DESAFIO035 dos triângulos, acresecetando o recurso de mostrar que tipo de triângulo será formado: Equilátero: todos os lados iguais. Isósceles: dois lados iguais. Escaleno: todos os lados diferentes

print("-=" * 20)
print("Analisador de trinângulos")
print("-=" * 20)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if (a == b and b == c and c == a):
    print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!")
elif (a != b and b != c and c != a):
    print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO!")
else:
    print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!")