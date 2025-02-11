import random
print('=' * 15)
print('VAMOS JOGAR')
print('=' * 15)


computador = random.randint(0, 10)
jogador = 0
palpite = 0

while jogador != computador:
    jogador = int(input('Advinhe o numero que pensei entre 1 e 10: '))
    palpite += 1

    if jogador < computador:
        print('TENTE UM NUMERO MAIOR. ')
    if jogador > computador:
        print('TENTE UM NUMERO MENOR. ')
print(f'PARABENS !!! Você acertou ! Eu pensei no numero {computador}')
print(f'Você precisou de {palpite} palpites para acertar.')