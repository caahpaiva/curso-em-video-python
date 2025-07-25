'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.
'''

def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :para num: uma ou mais notas dos alunos (aceita várias)
    :para sit: um valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    dicionario = {}
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['média'] = sum(num)/len(num)

    if sit == True:
        if dicionario['média'] >=7:
            dicionario['situação'] = 'BOA'
        
        elif dicionario['média'] >=5:
            dicionario['situação'] = 'RAZOÁVEL'
        else: 
            dicionario['situação'] = 'RUIM'
        
    return dicionario

# programa principal

resp = notas(3.5,2,6.5,2,7,4, sit=True)
print(resp)
# help(notas)