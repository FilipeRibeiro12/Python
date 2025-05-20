from time import sleep
numeros = list()
pergunta = 'S'

while pergunta == 'S':
  num = int(input('Digite um número: '))
  numeros.append(num)
  pergunta = str(input('Você dejesa digitar mais um número ? [S/N] ')).strip().upper()
  
  if pergunta != "S" and pergunta != "N":
    print('\033[31mPor favor digite uma alternativa válida\033[m')
    pergunta = str(input('Você dejesa digitar mais um número ? [S/N] ')).strip().upper()

  if pergunta == "N":
    print('Saindo do programa, Volte Sempre !')
    sleep(1)

print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse = True)
print(f'Essa é a lista da valores digitados de forma decrescente {numeros}')

if 5 in numeros:
  print('O número 5 está na lista.')
else:
  print('O número 5 não está na lista')
