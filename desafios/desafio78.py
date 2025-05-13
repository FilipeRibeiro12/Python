maior = 0
menor = 0
valores = list()
for cont in range(0, 5):
  valores.append(int(input(f'Digite um valor na posição {cont}: ')))
for c, v in enumerate(valores):
  if c == 0:
    maior = v
    menor = v
    posmaior = 0
    posmenor = 0
  else:
    if v > maior:
      maior = v
      posmaior = c
    if v < menor:
      menor = v
      posmenor = c
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi o {maior}, na posição {posmaior}')
print(f'O menor valor digitado foi o {menor}, na posição {posmenor}')
