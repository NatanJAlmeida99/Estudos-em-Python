# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5: Abaixo do Peso; Entre 18.5 e 25: Peso ideal; 25 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade mórbida


weight = float(input("Qual é seu peso? (Kg) " ))
height = float(input("Qual é sua altura? (m) "))
imc = weight / (pow(height, 2))
print(f"O IMC dessa pessoa é de {imc:.1f}")

if (imc < 18.5):
    print("Você está ABAIXO DO PESO normal")
elif (18.5 <= imc < 25):
    print("Você está com o PESO IDEIAL")
elif (25 <= imc < 30):
    print("Você está com o SOBREPESO")
elif (30 <= imc < 40):
    print("Você está com o OBESIDADE")
else:
    print("Você está com o OBESIDADE MÓRBIDA, cuidado")