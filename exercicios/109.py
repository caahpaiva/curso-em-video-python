'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas via ser ou não formatado pela função
moeda(), sedenvoldida no desafio 108.
'''

import moedas

p = float(input('Digite um preço: R$'))
print(f'A metade {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p,10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p,13, True)}')