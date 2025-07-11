'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para 
cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint 
from time import sleep

print('-'*30)
print(f'JOGA NA LOTOFÁCIL'.center(30))
print('-'*30)

palpites = int(input('Quantos jogos você quer que eu sorteie?: '))

jogos = []
jogo = []

for palpite in range(0,palpites):
  
    while len(jogo) < 15:
        num = randint(1,25)
        if num not in jogo:
            jogo.append(num)
    jogos.append(jogo[:])
    jogo.clear()



print('-='*3, end='')
print(f'  SORTEANDO {palpites} JOGOS  ', end='')
print('-='*3)


# Mostra os valores da matriz
for c, linha in enumerate(jogos):
    linha.sort()
    print(f'Jogo {c+1}: {linha}')
    sleep (1)
    
    


print('-='*5, end='')
print(' < BOA SORTE! > ', end='')
print('-='*5)



