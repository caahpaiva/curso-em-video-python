'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizar qual deles é o maior.
'''
from time import sleep

def maior(*num):
    print('-='*30)
    print(f'Analisando os valores passados...')
    sleep(0.5)
    tam = len(num)
    for v in num:
        print(f'{v} ', end='')
    print(f'Foram informados {tam} valores ao todo')
    maior_valor = max(num)
    print(f'O maior valor informado foi {maior_valor}')




maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)