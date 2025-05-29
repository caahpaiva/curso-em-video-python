'''
Faça um programa que calcule a soma entre todos os números ímpares que são 
múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

soma = 0   
cont = 0 
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:  # Verifica se é ímpar e múltiplo de 3
        cont += 1 # contador de números ímpares múltiplos de 3
        soma += c  # Adiciona o número à soma   

print("A soma dos {} números ímpares múltiplos de 3 no intervalo de 1 a 500 é:{}".format(cont,soma))