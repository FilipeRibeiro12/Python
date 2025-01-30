#Condição simples
nome = str(input('Qual é o seu nome ? '))

if nome == 'Filipe':
    print('Que nome lindo voce tem! ')
print(f'Bom dia {nome}')

#Condição composta
n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua media foi {m:.1f}')
if m >= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')