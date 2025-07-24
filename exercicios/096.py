'''
faça um programa que tenha uma função chamada área(), que receba as informações de
um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(largura, comprimento):
    area = largura*comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {area}m².')

print('Controle de Terrenos')
print('-'*20)


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l,c)