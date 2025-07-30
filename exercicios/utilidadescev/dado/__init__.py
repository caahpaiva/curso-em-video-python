
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: {entrada} é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(pergunta):
    valor = 0
    while True:
        resp = input(pergunta)
        if resp.isnumeric(): 
            valor = int(resp)         
            break
        else: 
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        
    return valor

