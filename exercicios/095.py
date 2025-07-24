'''
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogadores = []
resposta = 'S'

while resposta in 'S':
    jogador = {}
    total = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for i in range(0,partidas):     
        gol  = int(input(f'Quantos gols na partida {i}? '))
        gols.append(gol)
        total += gol
    jogador['gols'] = gols
    jogador['total'] = total
    jogadores.append(jogador)
    
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

print('-='*30)
print(jogadores)
print('-='*30)

print(f'cod nome   gols  total')
print('-'*30)

for c, va in enumerate(jogadores):
    print(f'{c} ', end='')
    for v in va.values():
        print(f'{v} ', end='')
    print()


view = 0

while view != 999:   
    print('-'*30)
    view = int(input('Mostrar dados de qual jogador? '))
    if view < len(jogadores):       
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[view]["nome"]}: ')
        for c, v in enumerate(jogadores):
            if view == c:
                
                for k, va in v.items():
                    if k == 'gols':
                        for q, g in enumerate(va):
                            print(f'No jogo {q} fez {g} gols.')
    else: 
         print(f'ERRO! Não existe jogador com código {view}!')



print('<< VOLTE SEMPRE >>')
