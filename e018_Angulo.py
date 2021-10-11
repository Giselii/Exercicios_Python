#Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno cosseno e tangente desse angulo

from math import radians, sin, cos, tan

angulo = float(input('Qual o angulo do triangulo: '))
sen = float(sin(radians(angulo)))
cos = float(cos(radians(angulo)))
tangente = float(tan(radians(angulo)))

print('O valor de seno de {} graus é {:.3f}'.format(angulo, sen))
print('O valor do cosseno de {} graus é {:.3f}'.format(angulo, cos))
print('O valor da tangente de {} graus é {:.3f}'.format(angulo, tangente))
