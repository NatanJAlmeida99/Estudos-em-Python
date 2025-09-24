# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
name = str(input("Digite seu nome completo: "))
split_name = name.split()
print(f"Muito prazer em te conhecer!\nSeu primeiro nome é {split_name[0]}\nSe útlimo nome é {split_name[len(split_name) - 1]}")