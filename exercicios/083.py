'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
abertos e fechados na ordem correta.
'''



frase = str(input('Digite uma expressão usando parênteses: '))
parentese = []


for v in frase:
    if v == '(':
        parentese.append('(')
    elif v == ')':
        if len(parentese) > 0:
            parentese.pop()
        else:
            parentese.append(')')
            break
    

if len(parentese)  == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
        

    