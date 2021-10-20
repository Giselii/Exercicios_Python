#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''n = int(input('Digite um número: '))
i = 2
fat = 1
while i <= n:
    fat = fat * i
    i = i + 1
print('{}! é igual a {}'.format(n, fat))'''

n = int(input('Digite um número para saber o fatorial: '))
cont = n
fatorial = 1
while cont > 0:
    print(cont)
    fatorial = (fatorial * cont)
    cont = cont - 1

print(fatorial)







