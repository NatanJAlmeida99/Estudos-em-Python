# Crie um programa de uma cidade e diga se ela começa ou não com o nome "SANTO"
city = str(input("Informe a cidade que você nasceu? ").upper())
print(city[:5] == 'SANTO')