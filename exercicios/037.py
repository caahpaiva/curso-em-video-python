''' Escreva um programa que leia um número inteiro qualquer e peça 
para o usuário escolher qual será a base de conversão: 
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

numero = int(input('Escreva o número que deseja converter: '))
escolha = int(input('Escolha para qual valor deseja converter: \n ' \
'1- binario \n 2- octal \n 3- hexadecimal: '))



if escolha == 1:
    binario = bin(numero)[2:]
    print('O número {} convertido para binario é {}'.format(numero, binario))

elif escolha == 2:
    octal = oct(numero)[2:]
    print('O número {} convertido para octal é {}'.format(numero, octal))

elif escolha == 3:
    hexadecimal = hex(numero)[2:].upper()
    print('O número {} convertido para hexadecimal é {}'.format(numero, hexadecimal))

else:
    print('Escolha uma opção válida')