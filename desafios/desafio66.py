n = s = c = 0
while True:
    n = int(input('Digite um número inteiro: [PARA PARAR DIGITE 999] '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} números e a soma entre eles é {s}')
