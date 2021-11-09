valor = int(input('Digite o valor:'))

milhares = valor//1000
centenas = (valor%1000)//100
dezenas = ((valor%1000)%100)//10
unidades = (((valor%1000)%100)%10)//1


print('O valor pode ser separado em:\nMilhares: {}\nCentenas: {}\nDezenas:{}\nUnidades: {}\n'.format(milhares, centenas, dezenas, unidades))

valor = str(valor)
print('Por string o valor pode ser separado em:\nMilhares: {}\nCentenas: {}\nDezenas:{}\nUnidades: {}\n'.format(valor[0], valor[1], valor[2], valor[3]))