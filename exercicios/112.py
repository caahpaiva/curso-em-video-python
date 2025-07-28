'''
Dentro do pacote utilidadesCeV que criamos no exercicio 111, temos um módulo chamado
dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a 
função input(), mas com uma validação de dados para aceitar apenas valores que sejam
monetários.
'''

from utilidadescev import moedas
from utilidadescev import dado

p = dado.leiaDinheiro('Digite o valor: R$')
moedas.resumo(p, 35,22)