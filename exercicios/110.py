'''
Adicone ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas inforamções geradas pelas funções que já temos no módulo
criado até aqui.
'''

from utilidadescev import moedas

p = float(input('Digite um preço: R$'))
moedas.resumo(p,80,35)