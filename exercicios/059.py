'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''

print('-=-' *10)
valor_um = float(input('Digite o primeiro valor: '))
valor_dois = float(input('Digite o segundo valor: '))
print('-=-' *10)

resultado_soma = valor_um + valor_dois
resultado_multi = valor_um * valor_dois

opcao = 0

while opcao != 5:
    opcao = int(input('''\n---- Digite uma das opções abaixo ----\n[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] sair do programa 
Opção:'''))
    if opcao == 1:
         print(f'\nRESULTADO: \nA soma de {valor_um} + {valor_dois} = {resultado_soma}')
    if opcao == 2:
        print(f'\nRESULTADO: \nA multiplicação de {valor_um} x {valor_dois} = {resultado_multi}')
    if opcao == 3:
        if valor_um > valor_dois:
            print(f'\nRESULTADO: \nO maior valor entre {valor_um} e {valor_dois} é {valor_um}')
        elif valor_um < valor_dois:
            print(f'\nRESULTADO: \nO maior valor entre {valor_um} e {valor_dois} é {valor_dois}')
        else: 
            print('\nRESULTADO: \nOs dois valores são iguais!')
    if opcao == 4:
        valor_um = float(input('\nDigite o primeiro valor: '))
        valor_dois = float(input('Digite o segundo valor:')) 
    if opcao > 5 or opcao == 0: 
        print('\nDigite uma opção válida.')   

print('\nFIM') 