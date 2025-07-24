'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da 
lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados 
pela função anterior.
'''

from random import randint

def sorteia():
    lista = []
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0,5):
        num = randint(1,10)
        lista.append(num)
        print(f'{num} ', end='')
    print('PRONTO!')
    
    return lista

def somaPar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lst}, temos {soma}')
    


sorteio = sorteia()
somaPar(sorteio)