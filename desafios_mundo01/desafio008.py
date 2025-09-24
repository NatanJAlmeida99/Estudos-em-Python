# Escrevar um programa que leia um valor em metros e o exiba convertido em centímetros a milímetros
dist = int(input("Uma distância em metros: "))
km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000
print(f"{km}km")
print(f"{hm}hm")
print(f"{dam}dam")
print(f"{dm}dm")
print(f"{cm}cm")
print(f"{mm}mm")