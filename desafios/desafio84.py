from time import sleep
dados = list()
pessoas = list()
maiorpeso = list()
menorpeso = list()
pergunta = 'S'

while pergunta == 'S':
  dados.append(str(input('Nome: ')))
  dados.append(float(input('Peso: ')))
  pessoas.append(dados[:])

  if dados[1] >= 100:
    maiorpeso.append(dados[:])
  elif dados[1] < 70:
    menorpeso.append(dados[:])

  dados.clear()

  pergunta = str(input('Você deseja cadastrar mais uma pessoa ? [S/N] ')).strip().upper()
  while pergunta not in ['S', 'N']:
      print('\033[31mPor favor digite uma alternativa válida\033[m')
      pergunta = str(input('Você deseja cadastrar mais uma pessoa ? [S/N] ')).strip().upper()

  if pergunta == 'N':
    print('Saindo...')
    sleep(1)

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
sleep(0.5)
print('pessoas com 100kg ou mais:')
for p in maiorpeso:
  print(f'{p[0]} com {p[1]}kg')
print('Pessoas com menos de 70kg:')
for p in menorpeso:
  print(f'{p[0]} com {p[1]}kg')