''' Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O Programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% 
do salário ou então o empréstimo será negado.'''


valor_casa = float(input('Qual é o valor da casa?'))
salario = float(input('Qual é o valor do seu salário? '))
anos = int(input('Em quantos anos você quer pagar?'))

mensal = valor_casa/(anos*12)
minimo = salario *30/100

print('Para pagar uam casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(mensal))

if mensal <= minimo:
    print('Empréstimo aprovado')
else:
    print("Empréstimo negado")