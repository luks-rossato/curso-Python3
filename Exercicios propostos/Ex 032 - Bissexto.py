ano = int(input("Digite o ano: "))

if ano%100 == 0 and ano%400 == 0:
    print('Bissexto!!')
else :
    if ano%4 == 0:

        print('Bissexto!!')
    else:
        print('Não é Bissexto!')
