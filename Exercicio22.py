# Analisador de texto
nome = str(input("Digite seu nome:").strip())
print('Nome em letras maiusculas: {}'.format(nome.upper()))
print('Nome em letras minusculas: {}'.format(nome.lower()))
print('Quantidade de letras sem espaço: {}'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Quantidade de letras no primeiro nome: {}'.format(len(separa[0])))
