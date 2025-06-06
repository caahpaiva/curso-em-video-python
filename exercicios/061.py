'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura While.
'''

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
limite = 1
pa = primeiro_termo

while limite <=10:
    print(pa, end=' -> ')
    pa += razao
    limite += 1
    

