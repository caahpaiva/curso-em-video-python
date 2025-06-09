'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

num = 0
contador = 0
soma = 0
maior = 0
menor = 0
media = 0
opcao = ''


while opcao != 'N':
    num = int(input("Digite um número: "))
    if contador == 1:
        menor = num
        maior = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    contador +=1
    media = soma/contador
    opcao = str(input('Você quer continuar [S]Sim/[N]Não:')).strip().upper()[0]

print(f'O maior número digitado foi {maior}, o menor foi {menor} e a média foi {media}')