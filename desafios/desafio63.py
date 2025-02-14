n = int(input('DIGA A QUNTIDADE DE ELEMENTOS DE UMA SEQUUENCIA DE FIBONACCI: '))

if n == 0:
    print('POR FAVOR DIGITE UM NUMERO MAIOR QUE 0')
else:    
    a, b = 0, 1
    cont = 0

while cont < n:
    print(a, end = ' --> ')
    a, b = b, a + b
    cont += 1
print('ACABOU')
    
