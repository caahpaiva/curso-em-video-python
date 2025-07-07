'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
escolha = 'S'
while escolha in 'S':
     lista.append(int(input('Digite um valor: ')))
     escolha = str(input('Quer continuar? [S/N]:')).strip().upper()[0]

print('-='*30)
print(f'Você digitou {len(lista)} elementos') # Conta o número de elementos na lista
lista.sort(reverse=True) # Ordena a lista de forma decrescente
print(f'Os valores em ordem decrescente são {lista}') 
if 5 in lista:
    print(f'O valor 5 foi encontrado pela primeira vez na posição {lista.index(5)}') # Encontra a posição na lista
else: 
     print('O valor 5 não foi encontrado na lista!')