'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''

frase = input("Digite uma frase: ").replace(" ", "").lower()
palindromo = frase == frase[::-1] # Inverte a string e compara
if palindromo:
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")    


frase2 = str(input("Digite uma frase: ")).strip().upper()
palavras = frase2.split()
junto = ''.join(palavras) 
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f"A frase '{frase2}' é um palíndromo.")    
else:
    print(f"A frase '{frase2}' não é um palíndromo.")