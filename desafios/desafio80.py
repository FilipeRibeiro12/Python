valores = list()
for n in range(0, 5):
  num = int(input('Digite um valor '))
  if valores == []:
    valores.append(num)
    print('Valor adicionado ao final da lista.')
  else:
    inserido = False
    for v in range(len(valores)):
      if num <= valores[v]:
        valores.insert(v, num)
        print(f'Valor inserido na posição {v}')
        inserido = True
        break
    if not inserido:
        valores.append(num)
        print('Valor inserido no final da lista')
print(valores)
      