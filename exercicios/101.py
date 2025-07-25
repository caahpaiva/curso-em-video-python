'''
Crie um programa que tenha uma função chamada voto() que vai receber um parametro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma 
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
'''



def voto(ano):
    from datetime import datetime # Posso importar somente dentro da função pra economizar memoria
    idade = datetime.now().year-ano
    
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade >= 18 and idade <=65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'
    

print('-'*30)
ano = int(input('Em que ano você nasceu? '))


print(voto(ano))
