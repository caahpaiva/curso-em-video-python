"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7.00 por cada km acima do limite.
"""

velocidade = float(input('Digite a velocidade do carro em KM:'))
limite = 80
multa = 7.00



if velocidade > limite:
    pagar = (velocidade-limite) * multa
    print('Você está acima da velocidade e foi multado, precisa pagar R$ {:.1f}'.format(pagar))
# elif velocidade >40 and velocidade <= 80:
#     print('Alerta!')    
else: 
    print('Você está dentro da velocidade permitida!')
    