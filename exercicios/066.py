'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
'''


soma = 0
cont = 0
n = 0

while True: # Laço infinito
    n = int(input("Digite um número (999 para parar): "))
    if n == 999:
        break # Quebra do laço
    soma += n
    cont += 1

print(f'Foram digitados {cont} vezes e a soma foi de {soma}')