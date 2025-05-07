"""
Crie um programa que leia um número inteiro e mostre na tela se ele
é PAR ou IMPAR
"""

numero = int(input("Digite um número: "))
validar = numero % 2
if validar == 0:
    print("O número {} que você digitou é PAR".format(numero))
else:
    print("O número {} que você digitou é IMPAR".format(numero))