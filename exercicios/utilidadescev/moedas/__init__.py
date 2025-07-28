def aumentar(n=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado valor,
    retornando o resultado com o seu formatação
    :param n: valor a ser aumentado
    :param taxa: a porcentagem pra aumentar
    param formato: quer a saida formatada ou não?
    return: retorna o valor reajustado, com ou sem formato.
    '''
    resp = n + (n * taxa/100)
    return resp if formato is False else moeda(resp)
     
def diminuir(n=0, taxa=0, formato=False):
    '''
    -> Calcula a redução de um determinado valor,
    retornando o resultado com o seu formatação
    :param n: valor a ser reduzido
    :param taxa: a porcentagem pra reduzir
    param formato: quer a saida formatada ou não?
    return: retorna o valor reajustado, com ou sem formato.
    '''
    resp = n-(n*taxa/100) 
    return resp if formato is False else moeda(resp)

def dobro(n=0, formato=False):
    '''
    -> Calcula o dobro de um valor com ou sem formato.
    :param n: valor a ser dobrado
    :param formato: quer a saída formatada ou não?
    return: o valor multiplicado por 2 com ou sem formato.
    '''
    resp = n*2
    return resp if formato is False else moeda(resp)

def metade(n=0, formato=False):
    '''
    -> Calcula a matade de um valor com ou sem formato.
    :param n: valor a ser dividido pela metade
    :param formato: quer a saída formatada ou não?
    return: o valor dividido por 2 com ou sem formato.
    '''
    resp = n/2
    return resp if formato is False else moeda(resp)

def moeda(valor=0, moeda = 'R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')


def resumo(n=0,aumento=10, menos=5):
    print('-'*30)
    print(f'    RESUMO DO VALOR'.center(30))
    print(f'-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n,aumento, True)}')
    print(f'{menos}% de redução: \t{diminuir(n, menos, True)}')
    print('-'*30)