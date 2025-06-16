#Mundo 3
#Variaveis Compostas (Tuplas)
# As tuplas são IMUTÁVEIS

# () = Tupla [] = Lista {} = Dicionario

lanche = ('Hamburguer', 'Suco','Pizza', 'Pudim')

print(lanche[1:]) # Vai do suco até o final
print(lanche[0:2]) #hamburguer e suco -- exclui a posição 2
print(lanche[2]) #suco -- mostra só a posição, no caso a pizza.
print(lanche[:-1]) #hamburguer até pizza -- exclui a ultima posição.
print(lanche[-2]) #Pizza, pega de trás pra frente


for c in lanche:
    print(c) #mostra cada linha da tupla


print(len(lanche)) #Mostra quantos itens tem na tupla (4)

for cont in range (0, len(lanche)):
    print(lanche[cont]) # Mostra o lanche na posição da contagem


    for pos, c in enumerate(lanche):
        print(c, pos) #mostra cada linha da tupla

print(sorted(lanche))


a = (2,5,4)
b = (5, 8, 1, 2)
c = a + b # Junta duas tuplas ex: 2,5,4,5,8,1,2
print(c.count(5))  # Mostra quantas vezes o número 5 aparece
print(c.index(8)) # Mostra a primeira posição que está o número 8


pessoa = ('Gustavo', 39, 'M', 99.88) # Pode ter mais de um tipo dentro da mesma tupla
print(pessoa)
del(pessoa) # Apaga a varial (informação)
del(pessoa[0]) #Não pode apagar um item da tupla por ela ser imutavel.

