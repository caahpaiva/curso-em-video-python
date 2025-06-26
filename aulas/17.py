#Mundo 3
#Variaveis Compostas (Listas)


lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

lanche[3] = 'picole' # Remove a informação que estava na posição e substitui pelo novo dado
lanche.append('biscoito') # Adiciona no final da lista
lanche.insert(0, 'cachorro quente') # Adiciona na posição informada

del lanche[3] # Remove a informação que existe na posição informada
lanche.pop[3] # Remove a informação que existe na posição informada
lanche.pop() # Elimina o ultimo item
lanche.remove('pizza') # Remove o item informado pelo conteudo , se  a informação não existe vai dar erro

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4,11)) #Vai contar do 4 até 10

valores = [8,2,5,4,9,3,0]
valores.sort() # Ordena do menor para o maior
valores.sort(reverse=True) # Ordena ao contrario(reverso) do maior para o menor
len(valores) # Conta quantos itens tem na lista

num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
num.remove(2) #Remove sempre a primeira ocorrencia 
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))


for c,valor in enumerate(valores):
    print(f'Na poição {c} encontrei o valor {valor}!')
print('Cheguei ao final da lista')


a = [2,3,4,7]
b = a # Liga uma lista com a outra
b[2] = 8 # Quando altera em uma lista, altera na A também
b = a [:] #Cria uma copia de A dentro de B

print(f'Lista A: {a}')
print(f'Lista B: {b}')


