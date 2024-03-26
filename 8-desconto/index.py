valor = float("Digite o valor do produto: ")
desconto = float("Digite o desconto: ")

precoDecimal = desconto / 100
precoFinal = valor * (1 - precoDecimal)

print("O valor do produto com desconto é: R$", precoFinal)
