n = int(input('Digite um valor:'))
count = 1
soma = n
maior = n
menor = n
continua = input('Quer continuar?[s/n]')
continua = 's'
while continua != 'n':
    n = int(input('Digite um valor:'))
    soma += n
    count += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continua = input('Quer continuar?[s/n]')
print('A média dos valores digitados foi: {}'.format(soma/count))