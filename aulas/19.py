#Mundo 3
#Variáveis compostas
#Dicionários 

dados = dict()
dados = {'nome': 'Pedro', 'idade':25}
print(dados[nome]) #resposta é Pedro
dados['sexo'] = 'M' # Criado e adicionado elemento no dicionario
del dados['idade'] # Elimina o elemento da estrutura


filme ={
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
}

print(filme.values()) #Retorna todos os valores = Star wars, 1977. George Lucas
print(filme.keys()) # Retorna os titulos
print(filme.items()) # Retorna tanto os valores e keys

for k, v in filme.items():
    print(f'O {k} é {v}') # o titulo é Star Wars, O Ano é 1977 

locadora = [{}, {}, {}] # Pode ter uma lista com varios dicicionarios dentro.

pessoas = {'Nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'{pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Leandro' # Altera de Gustavo pra Leandro
pessoas['peso'] = 98.5 # Adiciona novo item sem precisar de um append


for k in pessoas.kesy():
    print(k)

for v in pessoas.values():
    print(v)

for k,v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)  

print(brasil)
print(brasil[0]['uf']) # Mostra Rio de Janeiro
print(brasil[1]['siga']) # Mostra SP



estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Copia o item de um dicionario 

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

