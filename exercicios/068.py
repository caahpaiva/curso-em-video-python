'''
Faça um programa que jogue par ou impar com o computador. O jogo só será 
interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas 
que ele conquistou no final do jogo.
'''

import random

print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)

num = int(input("Digite um número: "))
escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
resultado_escolha = ''
resultado = 0
cont = 0
tipo = {'P': 'PAR', 'I': 'ÍMPAR'}


while True:
    pc = random.randint(0,10)
    resultado = pc + num
   
    if resultado % 2 == 0:
        resultado_escolha = 'P'              
    else:
        resultado_escolha = 'I'
    
    if escolha not in ('P', 'I'):
        num = int(input("Digite um número: "))
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    
    print('-'*20)
    print(f'Você jogou {num} e o computador {pc}. Total de {resultado} DEU {tipo[resultado_escolha]}')
    print('-'*20)

    if resultado_escolha == escolha:
        print('Você Venceu!')
        cont +=1
        num = int(input("Digite um número: "))
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    else:
        print('Você PERDEU!')
        break
            
print(f'GAME OVER! Você venceu {cont} vezes.')      
    
    



