s = 0 
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
print('Os numeros impares foram descartados. ')
print(f'Os numeros pares foram somados e o resultado foi: {s}')