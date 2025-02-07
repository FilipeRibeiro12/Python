t= int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for c in range(0, 10):
    termo = t + c * r
    print(termo)