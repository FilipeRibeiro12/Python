numeros = list()
pares = list()
impares = list()
for c in range(7):
  numeros.append(int(input(f'Digite o {c + 1}° numero: ')))
  for n in numeros:
    if n % 2 == 0:
      pares.append(n)
      numeros.clear()
    else:
      impares.append(n)
      numeros.clear()

pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print(f'Todos os valores digitados foram {numeros}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')