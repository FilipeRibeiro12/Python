from random import randint
print('-='*20)
print(' '*6,'VAMOS JOGAR PAR OU IMPAR ? ')
print('-='*20)
c = 0
while True:
    n = int(input('Digite um valor: '))
    jogador = str(input('Você escolhe par ou impar ? [P/I]')).strip().upper()[0]
    computador = randint(0, 10)
    soma = n + computador
    print(f'Você jogou {n} e o computador {computador}. Total de {soma} ', end='')
    if soma % 2 == 0:
        print('DEU PAR')
        if jogador == 'P':
            print('VOCÊ VENCEU!')
            print('-='*20)
            c += 1
        else:
            break
    elif soma % 2 == 1:
        print('DEU IMPAR')
        if jogador == 'I':
            print('VOCÊ VENCEU!')
            c += 1
            print('-='*20)
        else:
            break
print('-='*20)
print(f'GAME OVER! Você venceu {c} vezes')
