nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2

if media < 5.0:
    print(f'A sua media foi {media}, você foi reprovado.')
elif media > 7.0:
    print(f'A sua media foi {media}, você foi aprovado')
else:
    print(f'A sua media foi {media}, você está de recuperação')