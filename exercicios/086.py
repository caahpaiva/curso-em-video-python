'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos 
pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''

# Digite um valor para [0,0]

matriz = [[], [], []]
lista = len(matriz)
posicao = 0

while posicao < len(matriz):
    cont = 0
    while cont <3:
        num = int(input(f'Digite um valor para [{posicao}, {cont}]: '))
        matriz[posicao].append(num)
        cont +=1
    posicao += 1

# matriz = [[0,0,0], [0,0,0], [0,0,0]]
# for linha in range(3):
#     for coluna in range(3):
#         matriz[linha][coluna] = int(input(f'Digite um valor {linha}, {coluna}'))

print('-='*30)

for linha in matriz: 
    for valor in linha:
        print(f'[ {valor:^5} ]', end='')
    print()


