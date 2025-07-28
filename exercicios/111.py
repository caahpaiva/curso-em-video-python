'''
Crie um pacote chamado utilizadeCeV que tenha dois módulos internos chamados 
moeda e dado.
Transfira todas as funções utilizadas no desafios, 107,108 e 109 para o primeiro 
pacote e mantenha tudo funcionando.
'''

from utilidadescev import moedas

p = float(input('Digite um preço: R$'))
moedas.resumo(p,80,35)