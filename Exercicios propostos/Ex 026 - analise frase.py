frase = input('Digite uma frase:')

print('Aparece {} a letra "a"'.format(frase.count('a')))

print('A primeira vez que aparece é na posição {}'.format(frase.find('a')))
print('A ultima vez que aparece é na posição {}'.format(frase.rfind('a')))