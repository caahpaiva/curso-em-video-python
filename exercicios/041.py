''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER'''


from datetime import datetime

nascimento = int(input('Digite o ano do seu nascimento '))

ano = datetime.now().year
idade = ano-nascimento
print("Você tem {} anos de idade".format(idade))

if idade <= 9:
    categoria = "MIRIM"

elif idade >=10 and idade <=14:
    categoria = "INFANTIL"

elif idade >=15 and idade <=19:
    categoria = "JUNIOR"

elif idade >=20 and idade <=25:
    categoria = "SENIOR"

else:
    categoria = "MASTER"


print("Sua categoria é {}".format(categoria))