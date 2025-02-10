s = 0
cont = 0
print('Aqui estão os numeros impares multiplos de 3 entre 1 a 500')
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c 
        cont += 1
print(f' A soma dos {cont} numeros impares multiplos de 3, entre 1 a 500 é: {s}')
    