nome = str(input('Digite seu nome completo: '))
maisculo = nome.upper()
minusculo = nome.lower()
SemEspaço = nome.split()
quantidade_letras = len(nome.replace(' ', ''))
quantidade = len(SemEspaço[0])

print(f'''O seu nome com todas as letras maisuculas fica assim: {maisculo}
O seu nome com todas as letras minusculas fica assim: {minusculo}
A quantidade de letras no seu nome sem considerar os espaços é {quantidade_letras}: 
A quantidade de letras do seu primeiro nome é: {quantidade} ''')