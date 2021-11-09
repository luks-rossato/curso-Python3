sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo: [M/F]: ')).upper()

print('O sexo digitado foi: {}'.format(sexo))