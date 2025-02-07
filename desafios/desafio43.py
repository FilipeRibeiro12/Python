print('\033[1;31m-=-\033[m'*10)
print('Vamos calcular o seu IMC !!!')
print('\033[1;31m-=-\033[m'*10)
A = float(input('Digite sua altura: '))
P= float(input('Digite seu peso: '))
IMC = P / A ** 2

if IMC < 18.5:
    print(f'Seu calculo deu {IMC:.2f}, você está abaixo do peso.')
elif IMC <= 25:
    print(f'Seu calculo deu {IMC:.2f}, você está com o peso ideal.')
elif IMC <= 30:
    print(f'Seu calculo deu {IMC:.2f}, Você está com sobrepeso.')
elif IMC <= 40:
    print(f'Seu calculo deu {IMC:.2f}, você está com obesidade.')
else:
    print(f'O seu calculo deu {IMC:.2f}, você está com obesidade morbida.')
    