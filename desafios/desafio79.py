from time import sleep
pergunta = 'S'
valores = list()
while pergunta == 'S' or pergunta != 'N':
  valor = int(input('Digite um valor: '))
  if valor not in valores:
    valores.append(valor)
    print('\033[32mValor adicionado com sucesso!\033[m')
  else:
    print('\033[31mValor duplicado, não adicionado!\033[m')
  pergunta = str(input('Você deseja digitar mais um valor ? [S/N]')).strip().upper()
  while pergunta not in 'SN':
    print('Por favor digite uma alternativa válida')
    pergunta = str(input('Você deseja digitar mais um valor ? [S/N]')).strip().upper()
print('Saindo do programa...')
sleep(1)
valores.sort()
print(f'Você digitou os valores \033[33m{valores}\033[m')