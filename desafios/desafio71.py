from time import sleep

saldo = 0

print('-=-'*12)
print(' '*3,'BEM VINDO AO BANCO DO FILIPE')
print('-=-'*12)

while True:
    print('''
[1] PARA VER SALDO
[2] PARA SACAR 
[3] PARA DEPOSITAR
[4] PARA SAIR ''')
    
    pergunta = int(input('DIGITE UMA OPÇÃO: '))

    if pergunta == 1:
        print(f'SEU SALDO É DE R${saldo:.2f}')

    if pergunta == 2:
        print('PARA SAQUE TEMOS DISPONIVEIS NOTAS DE R$50, R$20, R$10 e R$1')
        valor = int(input('QUAL VALOR DESEJA SACAR? R$'))
        if valor > saldo:
            print('\033[31mSALDO INSUFICIENTE.\033[m')
        elif valor <= 0:
            print('\033[31mDIGITE UM VALOR VALIDO PARA SACAR\033[m')
        else:
            notas = [50, 20, 10, 1]
            saque = {}
            valor_restante = valor
            saldo -= valor
            for nota in notas:
                if valor_restante >= nota:
                    quantidade = valor_restante //nota # Quantidade de notas dessa cédula
                    saque[nota] = quantidade
                    valor_restante -= quantidade * nota

            print(f'Saque de R${valor} realizado com sucesso')

            for nota, quantidade in saque.items():
                print(f'{quantidade} nota(s) de R${nota}')

    if pergunta == 3:
        deposito = int(input('QUAL VALOR DESEJA DEPOSITAR ? R$'))
        saldo += deposito

    if pergunta == 4:
        print('FINALIZANDO...')
        sleep(1)
        break
print('-=-'*15)
print('OBRIGADO PELA PREFERENCIA, VOLTE SEMPRE')
print('-=-'*15)