nota1 = float(input("Digite sua AVP1: "))
nota2 = float(input("Digite sua AVP2: "))
media = (nota1 + nota2)/2
if media >= 7:
    print("APROVADO")
elif media >= 4:
    print("AVF")
else:
    print("REPROVADO")