'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma 
lista composta. No final, mostre um boletim contendo a média de cada um e permita 
que o usuário possa mostrar as notas de cada aluno individualmente. 
'''

lista_final = []
lista = []
resposta = 'S'

while resposta in 'S':
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    lista_final.append(lista[:])
    lista.clear()
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]



print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for n, aluno in enumerate(lista_final):
    media = 0
    print(f'\n {n:<4}', end='')
    for n, a in enumerate(aluno):
        if n == 1 or n == 2:
            media += a
        else:
            nome = a
        
    print(f'{nome:<10}{media/2:>8.1f} ', end ='')
        


print()
print('-'*30)


while True: 

    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('Finalizando...')
        break
    else:
        print(f'Notas de {lista_final[aluno][0]} são [{lista_final[aluno][1]}, {lista_final[aluno][2]}]')
        print('-'*30)


print('<<< VOLTE SEMPRE >>>')