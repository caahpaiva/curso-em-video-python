'''
Crie um programa que simula o funcionamento de um caixa eletronico. No
inicio, pergunte ao usuario qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas células de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

print('='*30)
print('{:^30}'.format('Banco CP'))
print('='*30)


valor = int(input('Qual valor quer sacar? R$'))
sacar = valor
ced_50 = 0
ced_20 = 0
ced_10 = 0
ced_1 = 0

while sacar != 0:
    if (sacar- 50) >= 0:
       sacar -= 50
       ced_50 += 1
    elif (sacar-20) >= 0:
        sacar -=20
        ced_20 += 1
    elif (sacar-10) >= 0:
        sacar -=10
        ced_10 += 1
    else:
        sacar -=1
        ced_1 += 1

if ced_50 > 0:
    print(f'Total de {ced_50} cédulas de R$50')
if ced_20 > 0:
    print(f'Total de {ced_20} cédulas de R$20')
if ced_10 > 0:
    print(f'Total de {ced_10} cédulas de R$10')
if ced_1 > 0:
    print(f'Total de {ced_1} cédulas de R$1')





# Exemplo do curso:
# total = valor
# ced = 50
# totalced = 0

# while True:
#     if total >= ced:
#         total -= ced
#         totalced += 1
#     else: 
#         if totalced > 0:
#             print(f'Total de {totalced} cédulas de R${ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totalced = 0
#         if total == 0:
#             break


print('='*30)
print('Volte sempre ao BANCO CP! Tenha um bom dia!')