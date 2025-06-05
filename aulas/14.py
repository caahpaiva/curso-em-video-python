# for c in range(1,10):
#     print(c)
# print(c)

# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print(c)


# for c in range(1,3):
#     n = int(input('Digite um valor: '))

# print('Fim')

# r = 'S'
# while n == 'S':
#     n = int(input('Digite um valor: '))
# print('Fim')

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Você digitou {par} números pares e {impar} números ímpares')