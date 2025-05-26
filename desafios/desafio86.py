matriz = list()
for l in range(0, 3):
  linha = list()
  for c in range(0, 3):
    linha.append(int(input(f'Digite um numero na posição[{l}][{c}]: ')))
  matriz.append(linha[:])
for i in matriz:
  for v in i:
    print(f'[{v:^5}]', end='')
  print()