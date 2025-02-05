velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade < 80:
    print('Você está dentro dos limites de velocidade')
else:
    print('Você foi multado pois ultrapassou os limites de velocidade')
    print(f'Você foi multado em R${multa:.2f}')