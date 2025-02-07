print('=-'*12)
print('VAMOS APRENDER A TABUADA')
print('=-'*12)
n = input('DIGITE UM NUMERO: ')

if n.isdigit():
    num = int(n)
    for c in range(0, 10,):
        print(f'{num} * {c} = { num * c }')
else:
    print('DIGITE SOMENTE NUMEROS')