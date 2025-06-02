'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

soma = 0
for num in range(1, 7):
    numero = int(input(f"Digite o {num}º número: "))
    if numero % 2 == 0:
        soma += numero
    else: 
        soma

print(f"A soma dos números pares digitados é: {soma}")