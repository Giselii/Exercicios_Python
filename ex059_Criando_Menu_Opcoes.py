#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
opcoes = 0
while opcoes != 5:
    opcoes = int(input('Escolha um número do menu para trabalhar os números: '))
    if opcoes == 1:
        print('A somas dos valores {} e {} é {}'.format(n1, n2, (n1 + n2)))
    elif opcoes == 2:
        print('O produto de {} e {} é {}'.format(n1, n2, (n1 * n2)))
    elif opcoes == 3:
       if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
       if n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
    elif opcoes == 4:
        print('Escolha novos valores para trabalhar')
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))

    else:
        print('Opção inválida!')

print('Você escolheu a opção 5. FIM DO PROGRAMA')
