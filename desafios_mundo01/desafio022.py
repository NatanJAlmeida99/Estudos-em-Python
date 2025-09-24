#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas / O nome com todas minúsculas / Quantas letras ao todo (sem considerar espaços) / Qunatas letras tem o primeiro nome
nome = str(input("Informe o seu nome completo: "))
name_upper = nome.upper()
name_lower = nome.lower()
nospace = nome.replace(" ", "")
name_split = nome.split()
print(f"Analisando seu nome...\nSeu nome em maiúscula é {name_upper}\nSeu nome em minúsculas é {name_lower}\nSeu nome tem ao todo {len(nospace)} letras\nSe primeiro nome é {name_split[0]} e ele tem {len(name_split[0])} letras")