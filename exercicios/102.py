'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será um valor
lógico(opcional) indicando se será mostrado ou não na tela o processo de 
cálculo do fatorial.
'''

def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :para n: O número a ser calculado.
    :para show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else: 
                print(' = ', end='')
        f *= i
    return f
    



print('-'*30)
print(f'{fatorial(5, show=True)}')
