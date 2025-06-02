'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''

frase = input("Digite uma frase: ").replace(" ", "").lower()
palindromo = frase == frase[::-1]
if palindromo:
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")    