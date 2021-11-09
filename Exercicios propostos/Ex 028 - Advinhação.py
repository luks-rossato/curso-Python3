import random

numero = random.randint(0,5)

esc = int(input('Escolha um número de 0 a 5:'))
if numero == esc :
    print('Parabéns, você Acertou!!!!')
else :
    print('Errou! o numero era o {}!'.format(numero))
