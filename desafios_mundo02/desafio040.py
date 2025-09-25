# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO Média entre 5.0 e 6.9: RECUPERAÇÃO Média 7.0ou superior: APROVADO

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print(f"Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media}")

if (media < 5):
    print("O aluno está de REPROVADO")
elif (5 > media > 6.9):
    print("O aluno está em RECUPERAÇÃO")
else:
    print("O aluno está APROVADO")