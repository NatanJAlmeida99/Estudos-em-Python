# Faça um programa que leia a largura e a altura de uma parede em mestros, caluclue a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
width = float(input("Largura da parede: "))
height = float(input("Altura dda parede: "))
area = width * height
paint = area / 2
print(f"Sua parede tem a dimensão de {width}x{height} e sua área é de {area}m²")
print(f"Para pintar essa árede, você precisará de {paint}l de tinta")