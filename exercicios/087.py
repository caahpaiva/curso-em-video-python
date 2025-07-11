'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha
'''


matriz = [[], [], []]
pares = 0

# Solicita os numeros e substitui a matriz já criada
for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f'Digite um valor [{linha}, {coluna}]: '))
        matriz[linha].append(num)
        if num % 2 == 0:
            pares +=num
          
# Mostra os valores da matriz
for linha in matriz:
    for valor in linha:
        print(f'[ {valor:^5} ]', end='')
        # if matriz[linha][coluna] % 2 ==0:
        #     somapar += matriz[linha][coluna] # outra forma de identificar e somar os pares

    print()

print('-='*30)

terceira = matriz[0][2] + matriz[1][2] + matriz[2][2] # Soma os valores da terceira coluna
# Outra maneira de somar somente as linhas da coluna
# for l in range(0,3):
#     somacoluna +=matriz[l][2]
segunda = max(matriz[1]) # Pega o maior valor da segunda linha
# outra maneira de pegar o maior
# for c in range(0,3):
#     if c == 0 or matriz[1][c] > maior:
#         maior = matriz[1][c]

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {segunda}')


