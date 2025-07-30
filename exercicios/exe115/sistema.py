'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e 
idade  em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas
cadastradas.
'''

from lib import interface
from lib import arquivo
from time import sleep


arq = 'exercicios\exe115\cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):    
    arquivo.criarArquivo(arq)


while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta  == 1:
        # Opção de listar o conteúdo de um arquivo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadatrar uma nova pessoa
        interface.cabecalho(f'NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho(f'Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)