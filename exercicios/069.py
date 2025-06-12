'''
Crie um programa que leia a idade e o sexo de várias pesssoas. A cada pessoa
cadastrada, o programa deverá perguntar se o úsuario quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

homens = 0
maior_18 = 0
mulher_menor = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    
    while sexo not in ('M', 'F'):
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    if sexo == 'M':
        homens += 1
    
    if idade >=18:
        maior_18 += 1

    if sexo == 'F' and idade < 20:
        mulher_menor += 1    

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
      
    if continuar == 'N':
        break
    
        

print('='*20)
print('FIM DO PROGRAMA')
print('='*20)

print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher_menor} mulheres com menos de 20 anos')