numeros = (int(input('Digite o primeiro numero: ')), 
           int(input('Digite o segundo numero: ')),
           int(input('Digite o terceiro numero: ')),
           int(input('Digite o quarto numero: ')))

print(f'Você digitou os valores: {numeros}')
print(f'O numero nove aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero tres aparece pela primeira vez na posição {numeros.index(3)+1}')
else:
     print('O valor 3 nao foi digitado em nenhuma posição')
print('Os valores pares são: ', end = '')
for n in numeros: 
    if n % 2 == 0 and n != 0:
       print(n, end=' ')