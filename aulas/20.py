#Funções
# Rotinas, coiass que acontecem com frequencia devem ser transformadas em funções.

def mostraLinha():
    print('------------------------------------')

mostraLinha()
print('SISTEMA DE ALUNOS')
mostraLinha()
mostraLinha()
print('CADASTRO DE FUNCIONÁRIOS')
mostraLinha()
mostraLinha()
print('ERRO DO SISTEMA')
mostraLinha()

def mensagem(msg):
    print('-------------------')
    print(msg)
    print('-------------------')

mensagem('SISTEMA DE ALUNOS')

def soma(a, b):
    r = a + b
    print(r)

soma(5,4)
soma(8,9)
soma(2,1)

def contador(*num): # * significa desempacotar, quando você não sabe quantos parametros tem
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')
    
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)



def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos +=1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)



def nova_soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


nova_soma(5,2)
nova_soma(2,9,4)