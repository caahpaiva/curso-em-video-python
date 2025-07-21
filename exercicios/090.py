'''
Faça um programa que leia nome e média de um aluno, guardando também a 
situação em um dicionario. No final mostre o conteúdo da estrutura na tela.
'''

aluno = {}


aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))


if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] <7:
    aluno['situação'] = 'Recuperação'
else: 
    aluno['situação'] = 'Reprovado'

for v, k in aluno.items():
    print(f'O {v} é igual a {k}')    