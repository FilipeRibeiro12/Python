nome = str(input('Qual é o seu nome ?'))
if nome == 'Filipe': # Condição simples
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': #Condição aninhada
    print('Seu nome é bem Popular no Brasil')
else: #Condição composta
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}')