'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o 
maior e o menor peso lidos.
'''

maior_peso = 0
menor_peso = 0 

for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i} (em kg): "))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:    
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso  
    

print(f"\nO maior peso lido foi: {maior_peso} kg")
print(f"O menor peso lido foi: {menor_peso} kg")
 
