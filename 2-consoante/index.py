letra = input("Digite um caractere: ").lower()

if letra.isalpha() and letra not in 'aeiou':
    print("O caractere digitado é uma consoante.")
else:
    print("O caractere digitado não é uma consoante ou não é uma letra.")
