''' Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento 

Seu programa também deverá mostrar o tempo que falta 
ou que passsou do prazo'''

from datetime import datetime

nascimento = int(input('Digite o ano do seu nascimento '))

ano = datetime.now().year
idade = ano-nascimento
print("Você tem {} anos de idade".format(idade))

if idade < 18:
    print("Você ainda vai se alistar, faltam {} anos".format(18-idade))
elif idade >=19:
    print("Você já passou {} anos do tempo do alistamento".format(idade-18))
else:
    print("Está na hora de você se alistar")

