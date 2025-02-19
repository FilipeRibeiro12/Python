from time import sleep
print('-'*55)
print(' '*10, 'BEM VINDO AO PROGRAMA DA TABUADA')
print('-'*55)

while True:
    print('PARA PARAR O PROGRAMA DIGITE QUALQUER NUMERO NEGATIVO')
    n = int(input('DIGITE UM NUMERO PARA VER SUA TABUADA: '))
    if n < 0:
        print('FINALIZANDO...')
        sleep(1)
        break
    c = 0
    print('-'*55)
    while c < 10:
        t = n * c
        print(f'{n} x {c} = {t}')
        c += 1
    print('-'*55)
print('VOCÊ SAIU DO PROGRAMA TABUADA, VOLTE SEMPRE !!!')
