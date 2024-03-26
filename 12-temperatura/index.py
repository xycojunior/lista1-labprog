print("Escolha a conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
escolha = int(input("Digite 1 ou 2: "))

if escolha == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é:", fahrenheit, "°F")
elif escolha == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("A temperatura em Celsius é:", celsius, "°C")
else:
    print("Escolha inválida. Por favor, digite 1 ou 2.")
