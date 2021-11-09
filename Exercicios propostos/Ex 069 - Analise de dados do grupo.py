idade = maiores = homens = beninas = 0
sexo = cont = ' '
print('VAMOS INICIAR O PROGRAMA')
while True:
    # while idade = int(input('Idade:')) <=0:
    idade = int(input('Idade:'))
    while sexo not in 'homem':
        sexo = str(input('Sexo:'))
    if idade >= 18:
        maiores += 1
    sexo = sexo.upper()
    if sexo == 'HOMEM':
        homens += 1
    if sexo == 'MULHER' and idade <= 20:
        beninas += 1
    while cont not in 'simnao':
        cont = input('Deseja continuar?[SIM/NAO]')
    cont = cont.upper()
    if cont == 'NAO':
        break
print(f"""OBRIGADO POR UTILIZAR NOSSO PROGRAMA!
Temos um total de {maiores} maiores de idade
temos {homens} homens no grupo e
temos {beninas} mulheres com menos de 20 anos!""")
