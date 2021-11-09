import random
print('''\033[7;31m===JOKENPô===\033[m

Para começar faça sua escolha:
- Pedra
- Papel
- Tesoura

O jogo acaba quando um jogador chegar a 3 pontos primeiro. Boa sorte!''')

ip = 0
ij = 0
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

while ip<3 and ij<3 :
    escolhaj = input('Jó Ken Pô:')
    escolhaj = escolhaj.upper()
    escolhapc = random.choice(opcoes)

    print('PLACAR:\nPC: {} x VOCÊ: {}'.format(ip, ij))

    print('PC: {}\nVocê: {}\n'.format(escolhapc, escolhaj))

    if escolhapc == escolhaj :
        print('\033[7;31mEMPATE!\033[m')
    elif escolhapc == 'PEDRA' and escolhaj == 'PAPEL' :
        print('Ponto para você!')
        ij = ij + 1
    elif escolhapc == 'PEDRA' and escolhaj == 'TESOURA' :
        print('Ponto para o PC!')
        ip = ip + 1
    elif escolhapc == 'PAPEL' and escolhaj == 'TESOURA':
        print('Ponto para você!')
        ij = ij + 1
    elif escolhapc == 'PAPEL' and escolhaj == 'PEDRA':
        print('Ponto para o PC!')
        ip = ip + 1
    elif escolhapc == 'TESOURA' and escolhaj == 'PEDRA':
        print('Ponto para você!')
        ij = ij + 1
    elif escolhapc == 'TESOURA' and escolhaj == 'PAPEL':
        print('Ponto para o PC!')
        ip = ip + 1
    else :
        print('\033[7,31m OPCÂO INVÀLIDA!\033[m\nTente novamente!')
