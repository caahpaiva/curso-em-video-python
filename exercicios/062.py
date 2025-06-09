'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar 
mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''


primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
pa = primeiro_termo
new_limite = int(input("Digite a quantidade de termos a mostrar: "))

while new_limite != 0:
    cont = 0
    while cont < new_limite:
        print(f'{pa}', end=' -> ')
        pa += razao
        cont += 1
        # limite += 1
    new_limite = int(input("Digite a quantidade de termos a mostrar: "))

print('Fim')
    


