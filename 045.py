''' "Crie um programa que faça o computador jogar Jokempô com você'''

import random
from time import sleep


opcoes = {1: "Papel", 2: "Tesoura", 3: "Pedra"}

jogador = int(input("Escolha uma número de acordo com a opção \n" \
" (1) Papel \n (2) Tesoura \n (3) Pedra: "))

if jogador not in opcoes:
    print("Opção inválida. Tente novamente com 1, 2 ou 3.")
else:
    computador = random.randint(1, 3)
    
    print("Computador escolhendo...")
    sleep(2)

    print(f"Você escolheu {opcoes[jogador]} e o computador {opcoes[computador]}.")


    if jogador == computador:
        resultado = "Empate, tente de novo!"
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        resultado = "Parabéns, você venceu!"
    else:
        resultado = "Você perdeu, tente de novo!"

    print(resultado)