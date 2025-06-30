'''
Faça um programa que leia 5 valores númericos e guarde os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas 
respectivas posições na lista.
'''

valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a poição {c}: ')))

maior = menor = valores[0]
posicao_maior = []
posicao_menor = []

for c, valor in enumerate(valores):
    if menor > valor:
        menor = valor
        posicao_menor = [c]
    elif menor == valor:
        posicao_menor.append(c)

    if maior < valor:
        maior = valor
        posicao_maior = [c]
    elif maior == valor:
        posicao_maior.append(c)

print('=-'*30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {maior} nas posições ', end ='')

for valor in posicao_maior:
    print(f'{valor}... ', end ='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end ='')

for valor in posicao_menor:
    print(f'{valor}... ', end ='')