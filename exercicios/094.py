'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados 
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, 
mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''

resposta = 'S'
qnt_pessoas = soma_idade = media =0
pessoas = []
mulheres = []
# maior_media = []


while resposta in 'S':
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    while True: 
        sexo = str(input('Sexo (M/F): ')).upper().strip()[0]
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    qnt_pessoas += 1
    soma_idade += pessoa['idade'] 
    media = soma_idade /qnt_pessoas
    
    
    pessoas.append(pessoa)
   
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]



# for k, v in enumerate(pessoas):
#     for ke, va in v.items():
#         if ke == 'idade':
#             if va > media:
#                 maior_media.append(v)


print('-='*30)
print(f'- O grupo tem {qnt_pessoas} pessoas')
print(f'- A média de idade é de {media:5.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for v in pessoas:
    if v['sexo'] == 'F':
        print(f'{v["nome"]} ', end='')
print()
print(f'- Lista das pessoas que estão acima da média: ')
for v in pessoas:
    if v["idade"] >= media:
        print('    ')
        for k, ve in v.items():
            print(f'{k} = {ve}; ', end='')

    


print('<<ENCERRADO >>')