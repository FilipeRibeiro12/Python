nome = str(input('Digite seu nome completo: ')).strip()
nome_dividido = nome.split()
primeiro_nome = nome_dividido[0]
ultimo_nome = nome_dividido[-1]

print(f'''O seu primeiro nome é {primeiro_nome}
O seu ultimo nome é {ultimo_nome}.''')
