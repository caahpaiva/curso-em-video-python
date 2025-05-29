# Laços de Repetição (Parte 1)
# Estrutura de repetição for


# i = int(input)("Inicio: ")
# f = int(input)("Fim: ")
# p = int(input)("Passo: ")

# for c in range(i, f+1, p):
#     print(c)

# print("FIM")

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n  # s = s + n 
print("O somatório de todos os valores foi {}".format(s))
