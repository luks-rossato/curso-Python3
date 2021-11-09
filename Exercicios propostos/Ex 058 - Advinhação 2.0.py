import random

count = 0
pc = 15
user = 14

while pc != user:
    pc = random.randint(0,10)
    user = int(input('Digite um número: '))
    if pc != user:
        print('Você errou! Vamos denovo!')
        count += 1
print('Você precisou de {} tentativas para acertar!, mas foi!'.format(count))
