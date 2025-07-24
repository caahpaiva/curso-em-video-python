'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável;
ex: escreva(Olá, Mundo!)
saída:
--------
Olá, mundo!
--------
'''

def escreva(texto):
    tam = len(texto) + 4
    print('~'*tam)
    print(f'  {texto}')
    print('~'*tam)

# Programa Principal
escreva('Olá, mundo!')
escreva('Curso em Python no Youtube')