import random
import time

print('=-='*10)
print('VAMOS JOGAR')
print('O jogo de hoje é o JOKENPÔ')
print('=-='*10)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(0.5)
if jogador == 0 or jogador == 1 or jogador == 2:
    print('-='*12)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-='*12)

    if computador == 0: # PEDRA
        if jogador == 0:
            print('DEU EMPATE')
        elif jogador == 1:
            print('VOCÊ GANHOU')
        elif jogador == 2:
            print('COMPUTADOR GANHOU')
    elif computador == 1: # PAPEL
        if jogador == 0:
            print('COMPUTADOR GANHOU')
        elif jogador == 1:
            print('DEU EMPATE')
        elif jogador == 2:
            print('VOCÊ GANHOU')
    elif computador == 2: # TESOURA
        if jogador == 0:
            print('VOCÊ GANHOU')
        elif jogador == 1:
            print('COMPUTADOR GANHOU')
        elif jogador == 2:
            print('DEU EMPATE')
else:
    print('JOGADA INVALIDA')
    