import random
import time

print('=-='*10)
print('VAMOS JOGAR')
print('O jogo de hoje é o JOKENPÔ')
print('=-='*10)

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
pensar = random.choice(jokenpo)

print('Escolha, PEDRA, PAPEL ou TESOURA')
escolha = input('').upper()
print('PROCESSANDO...')
time.sleep(2)


if pensar == 'PEDRA' and escolha == 'PAPEL':
    print(f'Eu pensei em {pensar}, você ganhou ')
elif pensar == 'PEDRA' and escolha == 'TESOURA':
    print(f'Eu pensei em {pensar}, eu ganhei')
elif pensar == 'PAPEL' and escolha == 'PEDRA':
    print(f'Eu pensei em {pensar}, eu ganhei')
elif pensar == 'PAPEL' and escolha == 'TESOURA':
    print(f'Eu pensei em {pensar}, voce ganhou')
elif pensar == 'TESOURA' and escolha == 'PEDRA':
    print(f'Eu pensei em {pensar}, você ganhou')
elif pensar == 'TESOURA' and escolha == 'PAPEL':
    print(f'Eu pensei em {pensar}, eu ganhei')
else:
    print(f'Nós pensamos em {pensar}, deu empate')