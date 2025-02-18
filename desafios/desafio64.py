cont = 999
n = 0
s = 0
c = 0
while n != cont:
    s += n
    n = int(input('DIGITE UM NUMERO: [999 para parar] '))
    if n != 0 and n != 999:
        c += 1
    print(n, end = ' --> ')
print(f'Foram digitados {c} numeros e a soma dos numeros digitados é {s}')