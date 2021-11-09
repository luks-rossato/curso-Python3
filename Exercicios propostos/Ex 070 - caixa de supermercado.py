valor = total = caros = valornor = 0
produto = nomenor = cont = ' '

while True:
    produto = str(input('Digite o nome do produto:'))
    valor = float(input('Digite o valor do produto:'))
    total += valor
    if valor > 1000:
        caros += 1
    if valornor == 0:
        valornor = valor
        nomenor = produto
    if valor < valornor:
        valornor = valor
        nomenor = produto

    cont = str(input('Quer continuar? [S/N]')).upper()
    if cont == 'N':
        break
print(f"""MUITO OBRIGADO POR USAR O PROGRAMA!
O total gasto na compra foi de R$ {total:.2f}
Temos {caros} produtos que custam mais de 1000 reais e
o produto mais barato foi o {nomenor} custando R${valornor:.2f}""")