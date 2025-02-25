from random import randint
cont = 0
maior = 0
menor = 0
while True:
    numeros = randint(0, 10)
    cont += 1
    print(f'Os valores sorteados foram: {numeros}', end=' ')
    if cont == 5:
        break
    if cont == 1:
        maior = numeros
        menor = numeros
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
print('')
print(f'O menor valor sorteado foi {menor}')
print(f'O maior valor sorteado foi {maior}')
