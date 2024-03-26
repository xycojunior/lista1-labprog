numero = int(input("Digite um número inteiro de 3 casas decimais: "))
centenas = int(str(numero)[0])
if centenas % 2 == 0:
    print("O algarismo da casa das centenas é par.")
else:
    print("O algarismo da casa das centenas é ímpar.")
