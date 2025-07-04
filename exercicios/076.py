'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,'Estojo', 25.00, 
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 
            'Canetas', 22.30, 'Livro', 34.90)
print('---'*20)
print(f'{'LISTAGEM DE PREÇO':^50}')
print('---'*20)

for produto in produtos:
    if isinstance(produto, str):
        nome = produto
        ponto = '.'* (30-len(nome))
        print(f'{nome}{ponto}R$', end ='')
    else:
        print(f'{produto:>7.2f}')




# for pos in range(0, len(produtos)):
#     if pos % 2 == 0:
#         print(f'{produtos[pos]:.<30}', end='')
#     else:
#         print(f'R${produtos[pos]:>7.2f}')