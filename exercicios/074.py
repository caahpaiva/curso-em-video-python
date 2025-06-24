'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla
'''


from random import randint

numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os valores sorteados foram: ', end='')
menor = min(numeros)
maior = max(numeros)


for n in numeros:
    print(f'{n} ', end='')



print(f'\nO maior número sorteado foi: {maior}')
print(f'O menor número sorteado foi: {menor}')


   

