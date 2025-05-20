from time import sleep
numeros = list()
pares = list()
impares = list()
pergunta = 'S'

while pergunta == 'S':
  num = int(input('Digite um número inteiro:'))
  numeros.append(num)
  pergunta = str(input('Você quer digitar mais um número? [S/N]')).strip().upper()

  if pergunta != 'S' and pergunta != 'N':
    print('Digite uma alternativa válida')
    pergunta = str(input('Você quer digitar mais um número? [S/N]')).strip().upper()

  if pergunta == 'N':
    sleep(1)
    print('Saindo do programa, volte sempre !')

for num in numeros:
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
print(f'Você digitou os seguintes valores {numeros}')
if pares == []:
  print('Você não digitou valores pares')
else:
  print(f'Os valores pares são {pares}')
if impares == []:
  print('Você nao digitou valores impares')
else:
  print(f'Os valores impares são {impares}')
  