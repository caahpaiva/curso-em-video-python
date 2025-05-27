''' Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros. 
'''



preco = float(input("Digite o valor do pedido: "))
pagamento = int(input("Digite o número de acordo com a forma de pagamento: \n" \
" (1) Á vista - Dinheiro/Cheque \n (2) Á vista - Cartão \n (3) Até 2x no cartão \n (4) 3x ou mais no cartão: "))

if pagamento == 1:
    valor = preco-(preco*(10/100))
    tipo = "Á vista - Dinheiro/Cheque"
elif pagamento == 2:
    valor = preco-(preco*(5/100))
    tipo = " Á vista - Cartão"
elif pagamento == 3:
    valor = preco
    tipo = "Até 2x no cartão"
elif pagamento == 4:
    valor = preco+(preco*(20/100))
    tipo = "3x ou mais no cartão:"
else: 
    tipo = "Inválida"
    valor = preco
    print("Escolha uma opção válida")
    

print("Como você escolheu a opção {} para pagamento, o valor a ser pago é {:.2f}".format(tipo, valor))