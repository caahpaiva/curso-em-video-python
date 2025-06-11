''' Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número
solicitado for negativo.'''


n = 1
resultado = 0

while True:
    n = int(input('Digite um número para ver a tabuada? '))  
    cont = 0 
    if n < 0:
       break
    else: 
        print('-'*30)
        print(f'A tabuada do número {n}: ')
        while cont <= 10:
            resultado = n*cont
            print(f'{n}x{cont} = {resultado}')
            cont += 1
        print('-'*30)
print(f'Fim')



# n = int(input('Digite um número para ver a tabuada? '))  
# resultado = 0
# cont = 0

# while True:
#     cont +=1
#     resultado = n * cont
#     print(f'{n}x{cont} = {resultado}')
#     if cont  == 10:
#        n = int(input('Digite um número para ver a tabuada? '))  
#        cont = 0
#     if n < 0:
#         break

# print('Fim')
   
