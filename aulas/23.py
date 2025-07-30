# Tratamento de Erros e Exceções

# Erro de sintaxe é quando você escreve errado, exemplo primt(), o comodando está errado;
# Exceção é quando você digita tudo certo mas não funciona. Ex, não tem uma variavel declarada ou foi informado um valor errado.
# Exceção: Outros exemplos é quando você divide por 0 que não existe. Uma string pra calculo.
# Comando: Exception - try: except: 

'''
try:
    operação que pode dar erro sendo uma exceção
except:
    o que deve acontecer caso a exceção aconteça.
except TypeError: # Você pode informar o tipo do erro e ter mais de um except
    o que deve acontecer caso a exceção aconteça.
except ValueError:
    caso tenha alguma falha
except OSError:
    caso tenha alguma falha (pode ter vários excepts)
else:
    o que fazer se o try der certo. (opcional)
finally:
    certo ou falha (opcional)
'''

# n = int(input('Número: '))
# print(f'Você digitou o número {n}')

# r = 2/0
# r = 2/'2'
# lst = [3,6,4]
# print(lst[3]) # Não existe a opção 3, vai somente até o 2. Mais uma exceção.


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except Exception as erro:
#     print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
     print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigada!')