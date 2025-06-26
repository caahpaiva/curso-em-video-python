'''
Faça um programa que leia 5 valores númericos e guarde os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas 
respectivas posições na lista.
'''

valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a poição {c}: ')))


for c, valor in enumerate(valores):
    if c == 0:
        menor = valor
        maior = valor
        posicao_maior = c 
        posicao_menor = c 
    else: 
        if menor >= valor:
                menor = valor
                posicao_menor = c
        if maior <= valor:
                maior = valor
                posicao_maior = c

print('=-'*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições {posicao_maior}...')
print(f'O menor valor digitado foi {menor} nas posições {posicao_menor}...')