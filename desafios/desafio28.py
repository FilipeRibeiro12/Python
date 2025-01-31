import random
import time

numeros = ['0', '1', '2', '3', '4','5']
pensar = random.choice(numeros)
escolha = str(input('Vou pensar num numero entre 0 e 5, tente advinhar. '))

print('PROCESSANDO...')
time.sleep(2)

if escolha == pensar:
    print('Parabens, você acertou o numero que pensei')
else:
    print(f'Você errou,eu pensei no numero {pensar} e nao no {escolha}, tente outra vez')