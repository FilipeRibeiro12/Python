import math

angulo = int(input('Digite um angulo '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f'O Seno de {angulo}° é: {seno:.2f} \n O Cosseno de {angulo}° é: {cosseno:.2f} \n A Tangente de {angulo}° é: {tangente:.2f}')

