'''
Crie um programa que tenha uma tupla totalmente 
preencida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.
'''


extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 
           'oito', 'nove', 'dez','onze', 'doze', 'treze', 'quatorze', 'quinze', 
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = 0

while True:
    num = int(input('Digite um número entre 0 a 20: '))
    if num >=21:
        print('Tente novamente')
    else: 
        print(extenso[num])
        break