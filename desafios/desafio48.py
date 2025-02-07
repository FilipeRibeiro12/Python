s = 0
print('Aqui estão os numero multiplos de 3 entre 1 a 500')
for c in range(1, 501):
    s = s + c
    if c % 3 == 0:
        print(c)
print(' A soma dos numeros multiplos de 3 entre 1 a 500 é:')
    