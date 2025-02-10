s = 0 
for c in range(1, 7):
    n = int(input(f'Digite o {c}° número inteiro: '))
    if n % 2 == 0:
        s += n
print('Os numeros impares foram descartados. ')
print(f'Os numeros pares foram somados e o resultado foi: {s}')