#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

produto = float(input('Qual o valor do produto: '))
print('====CONDIÇÕES DE PAGAMENTO====')
opcao = int(input('Ecolha a opcao de pagamnto. Digite o número referente a opção desejada: \n'
                  '1 - À vista\n'
                  '2 - À vista no cartão\n'
                  '3 - Em até duas vezes no cartão\n'
                  '4 -Em três vezes ou mais no cartão\n'
                  'Opção desejada: '))
um = produto - ((produto * 10) / 100)
dois = produto - ((produto * 5) / 100)
tres = produto
quatro = produto + ((produto * 20) / 100)

if opcao == 1:
    print('Pagando à vista, seu produto de R${} passa a custar R${}'.format(produto, um))
elif opcao == 2:
    print('Pagando à vista no cartão, seu produto de R${} passa a custar R${}'.format(produto, dois))
elif opcao == 3:
    print('Parcelando em até duas vezes no cartão, seu produto se mantém com o preço normal {}'.format(tres))
elif opcao == 4:
    print('Parcelando em três vezes ou mais no cartão, seu produto de R${} pasa a custar {}'.format(produto, quatro))