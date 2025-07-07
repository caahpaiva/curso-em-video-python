'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter os valores 
pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
resposta = 'S'
par = []
impar = []

while resposta in 'S':
    num = int(input('Digite um valor: '))
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)


# for i, v in enumerate(lista):
#     if v % 2 == 0:
#         par.append(v)
#     elif v % 2 == :
#         impar.append(v)




lista.sort()
par.sort()
impar.sort()

print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')