'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho 
- Quantas mulheres têm menos de 20 anos
'''



soma_idade = 0
media = 0
mais_velho = ''
idade_mais_velho = 0
mulheres_menor_20 = 0

for i in range(1, 5):
    nome = input(f"Digite o nome da {i}ª pessoa: ").strip()
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    sexo = int(input(f"Digite o sexo da {i}ª pessoa ([1] para Masculino /[0] para Feminino): "))

    soma_idade += idade
    media = soma_idade / i 

    if sexo == 1 and (idade > idade_mais_velho or i == 1):
        idade_mais_velho = idade
        mais_velho = nome

    if sexo == 0 and idade < 20:
        mulheres_menor_20 += 1
    
    


print(f"\nA média de idade do grupo é: {media:.2f} anos")
print(f"O homem mais velho é {mais_velho} com {idade_mais_velho} anos.")   
print(f"Total de mulheres com menos de 20 anos: {mulheres_menor_20}")     
