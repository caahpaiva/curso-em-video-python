'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves
'''
pesos = []
dados = []
informacoes = []
resposta = 'S'
totpessoa = 0
# pesomaior = []
# pesomenor = []


while resposta in 'S':
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pesos.append(peso)
    informacoes.append(dados[:])
    dados.clear()
    totpessoa += 1
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]


maior = max(pesos)
menor = min(pesos)

# for p in informacoes:
#     if p[1] == maior:
#         pesomaior.append(p[0])
#     elif p[1] == menor:
#         pesomenor.append(p[0])



print('-='*30)
print(f'Ao todo, você cadastrou {totpessoa} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in informacoes:
    if p[1] == maior:
        print(f'[{p[0]}] ', end= '')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in informacoes:
    if p[1] == menor:
        print(f'[{p[0]}] ', end= '')