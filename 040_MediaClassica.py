# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# 3- Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
from termcolor import colored
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
if media < 5:
    print(colored('Sua média é {}. REPROVADO. Estude mais!', 'red').format(media))
elif media >= 5 and media <= 6.9:
    print(colored('Sua média é {}. RECUPERAÇÃO! Você ainda tem uma chance!', 'yellow').format(media))
elif media >= 7:
    print(colored('Sua média é {}. APROVADO! PARABÉNS!', 'green').format(media))