'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionario se por acaso a CTPs for diferente de ZERO, o dicionario 
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar
'''
from datetime import datetime

func = {}

func['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
func['idade'] = idade

func['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if func['ctps'] != 0:
    func['contratação'] = int(input('Ano de contratação: '))
    func['salario'] = float(input('Salário: R$'))
    ano = 35-(ano_atual-func['contratação'])
    ano_aposentadoria = idade + ano
    func['aposentadoria'] = ano_aposentadoria 

print('-='*30)
print(func)
for k, v in func.items():
    print(f'- {k} tem o valor {v}')
