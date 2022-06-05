#Primeiro e ultimo nome de uma pessoa
nome = str(input('Digite seu nome completo:')).strip()
nome = nome.split()
print('O primero nome é {}\nO segundo nome é {}'.format(nome[0], nome[len(nome) - 1]))
