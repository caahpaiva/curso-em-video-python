'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
'''

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decima = primeiro_termo + (10 - 1) * razao

for c in range (primeiro_termo, decima + razao, razao):
    #termo = primeiro_termo + c * razao
    print(c, end=' -> ')

