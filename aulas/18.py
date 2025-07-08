#Mundo 3
#Listas Compostas 

dados = ['Pedro', 25, 'Maria', 19, 'João', 32]
pessoas = list ()
pessoas.append(dados[:]) # Adiciona uma lista na outra

pessoas = [['Pedro', 25], ['Maria',19], ['João', 32]] #Uma lista com outras listas dentro.

print(pessoas[0][0]) #Item 0 da lista na posição 0 mostra Pedro
print(pessoas[1][1]) #Mostraria 19 o item 1 da lista 1
print(pessoas[2][0]) #Mostra João, lista na posição 2 e item na posição 0
print(pessoas[1])    #Mostra a lista completa na posição 1 ['Maria', 19]


teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
# galera.append(teste) #Liga uma lista com a outra, quando altera um item na lista original altera na de ligação
galera.append(teste[:]) #Faz uma copia da lista teste pra dentro da lista galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade') #Mostra só os nomes e idade. 

# ---------------------------------------

galera = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # Limpa o que tiver na lista dados


print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')


