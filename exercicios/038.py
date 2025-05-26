''' Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior 
- Não existe valor maior, os dois são iguais'''

num_one = int(input('Digite o primeiro número:'))
num_two = int(input('Digite o segundo número:'))

if num_one > num_two:
    print('O primeiro valor é maior')
elif num_two > num_one:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')