'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''

num = int(input("Digite um número inteiro: "))
contador = 0
soma = 0 

while num != 999:
    contador += 1
    soma += num
    num = int(input("Digite um número inteiro: "))

print(f'Foram digitados {contador} vezes e a soma foi de {soma}')