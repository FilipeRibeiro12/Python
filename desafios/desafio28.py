import random

numeros = ['0', '1', '2', '3', '4','5']
pensar = random.choice(numeros)
escolha = str(input('Escolha um numero de 0 a 5: '))

if escolha == pensar:
    print('Parabens, você acertou o numero que pensei')
else:
    print('Você errou, tente outra vez')