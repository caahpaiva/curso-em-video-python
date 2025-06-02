'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
numero = int(input("Digite um número inteiro: "))
if numero < 2:
    print(f"{numero} não é um número primo.")   
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")