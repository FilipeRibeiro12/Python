n0 = 0
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
numeros = (n0, n1, n2, n3, n4)

print(f'O numero nove aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero tres aparece pela primeira vez na posição {numeros.index(3)}')
else:
     print('O valor 3 nao foi digitado em nenhuma posição')
for n in numeros: 
    if n % 2 == 0 and n != 0:
        pares = (n)
        print(f'Os numeros pares são {pares}')
