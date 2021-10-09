#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informaões possíveis sobre ele
#Usar os métodos .is


#OBSERVAÇÃO: Nos casos abaixo o 'a1' é um OBJETO e
#os ".is..." são os métodos.

a1 = input('Digite algo: ')
print('O tipo primitivo de {} é:'.format(a1), type(a1))
#print(float(a1), '= Em ponto flutuante')
print(bool(a1), '= Em boleano')
#print(int(a1), '= Em número inteiro')
print(str(a1), '= Em string')
print('É alfanumérico? (isalnum) = ', a1.isalnum())
print('Está em maiúscula? (isupper)? = ', a1.isupper())
print(a1.isalpha(), ' = É alfabeto? (isalpha)')
print(a1.isnumeric(), ' = É um número? (isnumeric)')
print(a1.isascii(), ' = isascii')
print(a1.isdecimal(), ' = isdecimal')
print(a1.isdigit(), ' = isdigit')
print(a1.isidentifier(), ' = isidentifier')
print(a1.islower(), ' = Está em minúscula? (islower)')
print(a1.isprintable(), ' = isprintable')
print(a1.isspace(), ' = Só tem espaco? (isspace)')
print(a1.istitle(), ' = Está capitalizada? (istitle)')
print(a1.__init_subclass__(), ' = __init_subclass__')

