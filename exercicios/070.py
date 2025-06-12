'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o úsuario vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
'''


print('-'*20)
print('CADASTRO DE PRODUTOS')
print('-'*20)

total = 0
mais_1000 = 0
cont = 0
produto_barato = ''
menor = 0

while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Valor: '))
    continuar = str(input('Quer continuar? [S/N]' )).upper().strip()[0]

    while continuar not in ('N', 'S'):
        continuar = str(input('Quer continuar? [S/N]' )).upper().strip()[0]

    total += preco
    cont += 1

    if preco >= 1000:
        mais_1000 += 1

    if cont == 1:
        menor = preco
        produto_barato = produto

    if preco <= menor:
        menor = preco
        produto_barato = produto

    if continuar == 'N':
        break

print('-'*20)
print('FIM DO PROGRAMA')
print('-'*20)
print(f'O total da compra foi {total}')
print(f'Temos {mais_1000} produtos custamos mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R$ {menor:.2f}')