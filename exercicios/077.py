'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('carolini', 'rodrigo', 'alec', 'wanessa', 'livia')




for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos: ', end = ' ')
    if  palavra.count('a') !=0:
         print(f'{palavra[palavra.index('a')]}', end=' ')
    if palavra.count('e') != 0:
        print(f'{palavra[palavra.index('e')]}', end=' ')
    if palavra.count('i') != 0:
        print(f'{palavra[palavra.index('i')]}', end=' ')
    if palavra.count('o') != 0:
        print(f'{palavra[palavra.index('o')]}', end=' ')
    if palavra.count('u') != 0:
        print(f'{palavra[palavra.index('u')]}', end=' ')
    


# for palavra in palavras:
#     print(f'\n Na palavra {palavra.upper()} temos: ', end = '')
#     for letra in palavra:
#         if letra.lower() in 'aeiou':
#             print(letra, end= ' ')