import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno: ')
alunos = [a1,a2,a3,a4]
ordem = random.sample(alunos, 4)

print(f'A ordem sorteada dos alunos é: {ordem}')