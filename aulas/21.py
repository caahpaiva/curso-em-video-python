#Funções parte 2

# Interactive help


help(print) # Ajuda interativa sobre a função print

print(input.__doc__) # Documentação sobre a função input

# Docstring 
# após a criação do def entre as 3x aspas duplas. 

def contador(i,f,p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param f: passo da contagem
    :return:  sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')

#contador(2, 10, 2)

help(contador)


# Paramentros opcionais
# Na declaração dos paramentros no def já atribuir o valor de 0.

def somar(a=0,b=0,c=0):
    s= a + b + c
    print(f'A soma vale {s}')



somar(3 ,2 ,5)
somar(8,4)
somar(b=2, c=1)

# Escopo de variais
# Local ou a variavel vai ou não existir.
# x é uma variavel local só funciona dentro da função
# n é uma variaval global porque foi declarada no programa principal.
# a dentro da função tem um valor e no programa principal tem outro.
# se declarar na função "global a" , o sistema começa a considerar a declaração no programa principal

def teste():
    global a
    x = 8
    a =  8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
    print(f'Na função teste, a vale {a}')

# Programa principal

n = 2 
a = 5
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}') o sistema da erro porque o x só foi declarado localmente na função.
print(f'No programa principal, a vale {a}')

teste()


# Retornando valores (Return)

def somando(a=0,b=0,c=0):
    s= a + b + c
    return s


r1 = somando(3,2,5)
r2 = somando(2,2)
r3 = somando(6)
print(f' Os resultados foram {r1}, {r2}, {r3}')


def fatorial(num=1):
    f =1 
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

numero = int(input('Digite um número: '))
if par(numero):
    print('É par!')
else:
    print('Não é par!')