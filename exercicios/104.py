'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
á função input() do python, só que fazendo a validação para aceitar apenas um valor
númerico.
Ex: n = leiaInt('Digite um n')
'''


def leiaInt(pergunta):
    valor = 0
    while True:
        resp = input(pergunta)
        if resp.isnumeric(): 
            valor = int(resp)         
            break
        else: 
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        
    return valor

print('-'*30)    
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
