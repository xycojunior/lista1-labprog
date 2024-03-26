numero = int(input("Digite um número: "))
quadrado = False
for i in range(int(numero ** 0.5) + 1):
    if i * i == numero:
        quadrado = True
        break

if quadrado:
    print("O número", numero, "é um quadrado perfeito.")
else:
    print("O número", numero, "não é um quadrado perfeito.")
