''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

altura = float(input("Digite sua altura (m): "))
peso = float(input("Digite o seu peso (Kg): "))


imc = peso /(altura**2)

if imc <=18.5:
    status = "Abaixo do peso"
elif imc >18.5 and imc <=25:
    status = "Peso ideal"
elif imc >25 and imc <=30:
    status = "Sobrepeso"
elif imc >30 and imc <=40:
    status = "Obesidade"
else:
    status = "Obesidade mórbida"

print("Conforme a sua altura de {} e seu peso {}, o seu IMC é {:.2F}, o que significa " \
"que você está com {}".format(altura, peso, imc, status))