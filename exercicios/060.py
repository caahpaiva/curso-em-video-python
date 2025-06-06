'''
Faça um programa que leia um número qualquer e mostre o seu fatorial
ex: 5! = 5x4x3x2x1 =120
'''

from math import factorial

num = int(input("Digite um número pra descobrir o fatorial: "))
f = factorial(num)
print(f'O fatorial de {num} é {f}') # Solução simples do python com modulo



fatorial_for = num

print('\n','-=-' *10)
print(f'Fatorial com FOR')
print('-=-' *10)
for i in range(num-1,0,-1):
    fatorial_for = fatorial_for * i
    # print(f' {num} x {num-1} = {num*num-1}')
    print(f' {i} x {int(fatorial_for/i)} = {fatorial_for}')
    
print(f' O fatorial de {num} é: {fatorial_for}')

print('\n','-=-' *10)
print(f'Fatorial com WHILE')
print('-=-' *10)

div = num-1
fatorial = num

while div > 0:
    fatorial =  fatorial * div
    print(f' {div} x {int(fatorial/div)} = {fatorial}')
    div -= 1  
    

print(f' O fatorial de {num} é: {fatorial}')