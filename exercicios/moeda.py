def aumentar(n=0, taxa=0):

    return n + (n * taxa/100)
     
def diminuir(n=0, taxa=0):
    return n-(n*taxa/100) 

def dobro(n=0):
    return n*2 

def metade(n=0):
    return n/2

def moeda(valor=0, moeda = 'R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.',',')