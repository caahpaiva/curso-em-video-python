'''
Melhore o jogo do Defafio 028 onde o computador vai "pensar" em um 
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.
'''

import random
from time import sleep

print('-=-' *20)
print('Vamos jogar, vou pensar em um número entre 0 a 10. Tente adivinhar...')
print('-=-' *20)

pc = random.randint(0,10) #Sortear um número entre 0 a 10
palpite = 1 #Contador de vezes que o usuario respondeu

usuario = int(input('Em que número eu pensei?: '))

print('PROCESSANDO...')
sleep(1)

while usuario != pc:
    usuario = int(input('Poxa, você não acertou! Tente de novo: '))
    palpite += 1
    print('PROCESSANDO...')
    sleep(1)

print(f'Parabéns, você venceu em {palpite} palpites!')
