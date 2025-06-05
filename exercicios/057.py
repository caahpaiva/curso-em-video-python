'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = ''
while sexo not in ['F', 'M']:
    sexo = input('Digite o seu sexo [M/F]: ').upper().strip()[0]

print(f'O sexo digitado foi {sexo}')


# sexo = input('Digite o seu sexo [M/F]: ').upper().strip()[0]

# while sexo not in ['F', 'M']:
#     sexo = input('Dados inválidos. Por favor, digite o seu sexo [M/F]: ').upper().strip()[0]

# print(f'O sexo digitado foi {sexo}')
