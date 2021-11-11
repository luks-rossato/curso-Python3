times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza',
         'Bragantino', 'Corinthians', 'Internacional' 'Fluminense',
         'Athetico-PR', 'América-MG', 'Cuiabá', 'Ceará',
         'Santos', 'São Paulo', 'Atlético-GO', 'Bahia',
         'Juventude', 'Sport', 'Grêmio', 'Chapecoense')

print('Vou te mostrar alguns dados do Campeonato Brasileiro!')
print('Os cinco primeiros colocados são:')
print(times[0:6])
print('Os candidatos a rebaixamento são:')
print(times[-5:])
print('Os times em ordem alfabética são:')
print(sorted(times))
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª Posição')