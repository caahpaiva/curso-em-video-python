'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e impares. No final, 
mostre os valores pares e ímpares em ordem crescente.
'''

lista = [[], []]
# par = []
# impar = []

for c in range(1,8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 ==0:
        lista.append(num)
        lista[0].append(num)
    else:
        impar.append(num)
        lista[1].append(num)

lista[0].sort()
lista[1].sort()
# lista.append(par[:])
# lista.append(impar[:])


print('-='*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
