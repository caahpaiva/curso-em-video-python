#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input("Digite em cm o tamanho da primeira reta: "))
r2 = int(input("Digite em cm o tamanho da segunda reta: "))
r3 = int(input("Digite em cm o tamanho da terceira reta: "))


if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
   print("Com as retas informadas é possivel formar um triângulo")

else:
    print("Você não pode formar um triangulo com as retas informadas") 