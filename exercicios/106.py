'''
Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar 
o comdando e o manul vai aparecer. Quando o usuário digitar a palavra 'FIM', o 
programa se encerrará. OBS: use cores.
'''
from time import sleep

c = ('\033[m',           # 0 - sem cores
     '\033[0;30;41m',     # 1 - vermelho
     '\033[0;30;42m',    # 2 - verde
     '\033[0;30;43m',    # 3 - amarelo
     '\033[0;30;44m',    # 4 - azul
     '\033[0;30;45m',    # 5 - roxo
     '\033[7;30m',       # 6 - branco
     )

def consulta(func):
    titulo(f'Acessando o manual do comando \'{func}\'',4)
    print(c[5], end='')
    help(func)
    print(c[0], end='')
    sleep(2)

def titulo(msg,cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 6)
    resp = str(input('Função ou Biblioteca> ')).strip().lower() 
    print('~'*40)
    print(f'  Acessando o manul do comodando {resp}')
    print('~'*40)   
    if resp.upper() == 'FIM':
        break
    else:
        consulta(resp)
titulo('ATÉ LOGO!', 6)


