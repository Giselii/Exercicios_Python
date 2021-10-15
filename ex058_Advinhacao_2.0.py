#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
ncomp = random.randint(1, 10)
cont = 0
n = 0
while n != ncomp:
    n = int(input('Digite um número para tentar advinhar: '))
    cont = cont + 1
    if ncomp > n:
        print('Mais...')
    if ncomp < n:
        print('Menos...')
print('Foram necessárias {} tentativas para acertar. O número sorteado é {}'.format(cont, ncomp))
