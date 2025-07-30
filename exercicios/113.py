'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número de tipo inválido. Aproveite e crie também
uma função leiaFloat() com a mesma funcionalidade.
'''


def leiaInt(msg):
    
    while True:
        try: 
            resp = int(input(msg)) 
        except (ValueError, TypeError):
            print('\033[0;31mEERRO: Por favor, digite um número inteiro válido.\033[m')
            continue  
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:         
            return resp




def leiaFloat(msg):
    while True:
        try:
            resp = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mEERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return resp


print('-'*30)    
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n} que é inteiro')    
num = leiaFloat('Digite um número qualquer: ')
print(f'Você acabou de digitar o número {num} que é float')