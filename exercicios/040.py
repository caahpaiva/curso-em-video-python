''' Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5,0: REPROVADO
- Média entre 5,0 e 6,9: RECUPERAÇÂO
- Média 7,0 ou superior: APROVADO '''


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2

if media < 5.0:
    print('Sua média foi {} e você está REPROVADO'.format(media))
elif media >=5.0 and media <=6.9:
    print('Sua média foi {} e você está de RECUPERAÇÂO'.format(media))
else:
    print('Sua média foi {} e você está APROVADO'.format(media))