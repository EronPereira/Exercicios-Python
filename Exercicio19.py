# Sorteio de item
import random
aluno1 = input('Primeiro Aluno:')
aluno2 = input('Segundo aluno:')
aluno3 = input('Terceiro aluno:')
aluno4 = input('Quarto aluno:')
sort = aluno1, aluno2, aluno3, aluno4
escolhido = random.choice(sort)
print('O escolhdo foi: {}'.format(escolhido))
