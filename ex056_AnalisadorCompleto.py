#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
velho = 0
id = 0
nomevelho = ''
idademulher = 0
contidademulher = 0
for c in range(1, 5):
    print('======== {}ª PESSOA ==========='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: '))
    id = id + idade

    if c == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contidademulher = contidademulher + 1

media = id / c
print('A média de idade do grupo é {}: '.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
print('O número de mulheres com menos de 20 anos de idade é de {}'.format(contidademulher))