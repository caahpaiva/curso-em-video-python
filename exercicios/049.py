'''
Refaça o desafio 009, mostrando a tabuada de um número que o úsuário escolher, 
só que agora utilizando um laço for.
'''

num = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}") 
