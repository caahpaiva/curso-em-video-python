''' Reçafa o DESAFIO 035 dos triângulos, acrescentando o recurso de 
mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes '''


r1 = int(input("Digite em cm o tamanho da primeira reta: "))
r2 = int(input("Digite em cm o tamanho da segunda reta: "))
r3 = int(input("Digite em cm o tamanho da terceira reta: "))


if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    if r1 == r2 and r2 == r3:
        tipo = "Equilátero"
    elif (r1 == r2 and r1 != r3) or (r2 == r3 and r1 != r3) or (r1 == r3 and r2 != r3):
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print("Você conseguiu formar um triangulo {}".format(tipo))

else:
    print("Você não pode formar um triangulo") 
