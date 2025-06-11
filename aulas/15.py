# Laços de Repetição (Parte 3)


n = s = 0
while True: # Laço infinito
    n = int(input("Digite um número: "))
    if n == 999:
        break #Interrompe o laço
    s += n
print('Acabou')
