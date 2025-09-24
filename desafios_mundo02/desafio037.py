# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
num = int(input("Digite um número inteiro: "))
print('''Escolha uma das base para conversão:
      [1] converte para BINÁRIO
      [2] converte para OCTAL
      [3] converte para HEXADEMCIMAL''')

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para HEXADECIMA é igual a {hex(num)[2:]}")
else:
    print("Opção inválida")