'''
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que 
consiga mostrar os valores como um valor monetário formatado.
'''

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}')