# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
name = str(input("Informe seu nome completo: ").upper())
silva_in_name = "SILVA" in name
print(f"Seu nome tem Silva? {silva_in_name}")