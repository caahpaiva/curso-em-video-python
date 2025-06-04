'''
Crie um programa que leia o ano de nascimento de sete pessoas.
E mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import datetime

ano_atual = datetime.datetime.now().year  # Obtém o ano atual

maior = 0
menor = 0

for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i + 1}: "))
    idade =  ano_atual - ano_nascimento # calcula a idade
    if idade < 21:
        menor += 1
        print(f"A pessoa {i + 1} tem {idade} anos e ainda não atingiu a maioridade.")
    else:
        maior += 1
        print(f"A pessoa {i + 1} tem {idade} anos e já é maior de idade.") 

print(f"\nTotal de pessoas que ainda não atingiram a maioridade: {menor}")
print(f"Total de pessoas que já são maiores de idade: {maior}")