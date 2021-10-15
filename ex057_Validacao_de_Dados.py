# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Qual o sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Qual o sexo [F/M]: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso'.format(sexo))
print('FIM')

