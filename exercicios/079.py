'''
Crie um programa onde o usuário possa digitar vários valores númericos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''


valores = []

opcao = 'S'
while opcao in 'S':
    valor = (int(input(f'Digite um valor: ')))
    if valor not in valores:
        valores.append(valor) 
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
         

    opcao = str(input('Quer continuar? [S/N]:')).strip().upper()[0]

valores.sort()

print('Você digitou os valores: ', end='')
for num in valores:
     print(f'{num}... ', end ='' )
    