print('-='*20)
print('Bem vindo a tabela do brasileirão 2025')
print('-='*20)

times = ('Atletico-MG', 'Bahia', 'Botafogo', 'Ceara SC', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Gremio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife', 'São Paulo', 'Vasco da Gama', 'EC Vitoria')

while True:
    print('[1] Lista dos times')
    print('[2] Os 5 primeiros times') 
    print('[3] Os 4 ultimos times')
    print('[4] Times em ordem alfabetica')
    print('[5] Posição do time Cruzeiro')
    print('[6] Sair')
    escolha = int(input('Escolha uma das opções para saber sobre a tabela '))

    if escolha == 0 or escolha > 6:
        print('\033[31mEscolha uma alternativa valida\033[m')
        print('[1] Lista dos times')
        print('[2] Os 5 primeiros times') 
        print('[3] Os 4 ultimos times')
        print('[4] Times em ordem alfabetica')
        print('[5] Posição do time Cruzeiro')
        print('[6] Sair')
        escolha = int(input('Escolha uma das opções para saber sobre a tabela '))
        print('\033[31mEscolha uma alternativa valida\033[m')
    if escolha == 1:
        print(f'a lista de times do Brasileirão é {times}')
    if escolha == 2:
        print(f'Os 5 primeiros times são: {times[0:5]}')
    if escolha == 3:
        print(f'Os 4 ultimos são: {times[16:]}')
    if escolha == 4:
        print(f'Os times em ordem alfabetica são: {sorted(times)}')
    if escolha == 5:
        print(f'A posição do time do cruzeiro é: {times.index('Cruzeiro')}')
    if escolha == 6:
        break
print('-='*20)
print('Volte Sempre a tabela do brasileirão 2025')
print('-='*20)
