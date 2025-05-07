"""
Desenvolva um programa que pergunte a distancia de uma viagem em KM.
Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens até 200Km
e R$ 0,45 para viagens mais longas.
"""

km = float(input("Qual é a distancia em KM da sua viagem?"))
limite = 200
tarifa_1 = 0.50
tarifa_2 = 0.45

if km <=limite:
    pagar = km * tarifa_1
    print("Será cobrado R$ 0.50 por KM e você vai pagar R${} pelos {} km da viagem".format(pagar, km))
else: 
    pagar = km * tarifa_2
    print("Será cobrado R$ 0.45 por KM e você vai pagar R${} pelos {} km da viagem".format(pagar, km))

