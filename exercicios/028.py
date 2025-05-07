"""
Escreva um programa que faça o computador "pensar" em um número inteiro 
entre 0 a 5 a peça para o usuário tentasr descobrir qual foi o número 
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu
"""

import random
from time import sleep

pc = random.randint(0,5) #Sortear um número entre 0 a 5

print('-=-' *20)
print('Vamos jogar, vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' *20)
usuario = int(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
sleep(3)
print('Você escolheu o número: {} e eu pensei no número: {}'.format(usuario, pc))
if pc == usuario:
    print('Parabéns, você venceu!')
else: 
    print('Poxa, você perdeu! Tente de novo')