'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequencia de fibonacci.
Ex: 0 - 1 -1 - -2 -3 -5 -8 
'''

seq = int(input('Digite quantos números você quer na sequencia: '))
termo1 = 0
termo2 = 1 
contador = 3

print(f' Os {seq} primeiros números de uma sequencia Fibonacci são: ')
print( '0 -> 1', end='')
while contador <= seq:
    pos = termo1+termo2
    print(f" -> {pos}", end='')
    termo1 = termo2
    termo2 = pos
    contador += 1