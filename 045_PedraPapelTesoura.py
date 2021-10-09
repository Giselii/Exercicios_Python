#Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
import random
from termcolor import colored
print(colored('=', 'red') * 8, colored('VAMOS JOGAR JOKENPÔ', 'blue'), colored('=', 'red') * 8)
usuario = str(input(colored('Qual sua jogada: ', 'green')))

sleep(1)
print(colored('JO..', 'blue'))
sleep(1)
print(colored('KEN..', 'blue'))
sleep(1)
print(colored('PÔ!!', 'blue'))
pedra = str('pedra')
papel = str('papel')
tesoura = str('tesoura')
op = [pedra, papel, tesoura]
computador = random.choice(op)
if computador == papel and usuario == tesoura:
    print(colored('O computador jogou {} e voce jogou {}. Você venceu!', 'yellow').format(computador, usuario))
elif computador == papel and usuario == pedra:
    print(colored('O computador jogou {} e você jogou {}. O computador venceu!', 'yellow').format(computador, usuario))
elif computador == tesoura and usuario == papel:
    print(colored('O computador jogou {} e você jogou {}. o computador venceu!', 'yellow').format(computador, usuario))
elif computador == tesoura and usuario == pedra:
    print(colored('O computador jogou {} e você jogou {}. Você venceu!', 'yellow').format(computador, usuario))
elif computador == pedra and usuario == papel:
    print(colored('O computador jogou {} e você jogou {}. Você venceu!', 'yellow').format(computador, usuario))
elif computador == pedra and usuario == tesoura:
    print(colored('O computador jogou {} e você jogou {}. O computador venceu!', 'yellow').format(computador, usuario))
elif (computador == pedra and usuario == pedra) or (computador == papel and usuario == papel) or (computador == tesoura and usuario == tesoura):
    print(colored('o computador jogou {} e voce {}. EMPATE!!', 'yellow').format(computador, usuario))


