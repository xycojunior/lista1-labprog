num1 = int(input("Digite o 1 número: "))
num2 = int(input("Digite o 2 número: "))
num3 = int(input("Digite o 3 número: "))
if num1 < num2 and num1 < num3:
    print(num1, "é o menor!")
elif num2 < num1 and num2 < num3:
    print(num2, "é o menor!")
elif num3 < num1 and num3 < num2:
    print(num3, "é o menor!")
else:
    print("Os números são iguais")