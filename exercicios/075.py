'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde=os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares
'''


numeros = (int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: ')),
           int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: ')))

print(f'Você digitou os valores: {numeros}')

print(f'O número 9 apareceu {numeros.count(9)} vezes')


if 3 in numeros:
    print(f'O número 3 apareceu primeiro na {numeros.index(3)+1} ª posição')
else: 
     print(f'O número 3 não aparece em nenhuma posição')

print('Os valores pares digitados foram:', end='')
for n in numeros:
     if n % 2 == 0:
          print(n, end=' ')