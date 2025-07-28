#from uteis import fatorial, dobro # Formato não muito remcomendado porque pode ter conflito entre as funções
#import  uteis # Formato mais recomendado.
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}')