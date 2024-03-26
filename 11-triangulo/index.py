lado1 = float(input("Digite o 1 lado do triângulo: "))
lado2 = float(input("Digite o 2 lado do triângulo: "))
lado3 = float(input("Digite o 3 lado do triângulo: "))

if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles.")
else:
        print("É um triângulo escaleno.")