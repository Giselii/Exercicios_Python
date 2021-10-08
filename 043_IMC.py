#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
#Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
from termcolor import colored
print(colored('======== CALCULANDO IMC ========', 'blue'))

peso = float(input('Seu peso: '))
alt = float(input('Sua altura: '))
imc = (peso / (alt**2))
if (imc > 18.5) and (imc < 25):
    print('Seu IMC é de  {:.2f}. PESO IDEAL'.format(imc))
elif (imc > 25) and (imc < 30):
    print('Seu IMC é de {}. SOBREPESO'.format(imc))
elif (imc > 30) and (imc < 40):
    print('Seu IMC é de {}. OBESIDADE!!'.format(imc))
elif imc > 40:
    print('Seu IMC é de {}. OBESIDADE MÓRBIDA'.format(imc))


