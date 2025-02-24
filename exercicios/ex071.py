valor = int(input('Qual valor deseja sacar ? R$'))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if ced > 0:
            print(f'Total de {totalced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('VOLTE SEMPRE!')

