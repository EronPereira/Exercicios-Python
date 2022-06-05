import random
from time import sleep
print(' / \ ' * 20)
print('/   \ ' * 20)
num1 = int(input('Advinhe um número entre 0 e 5: '))
num2 = random.randint(0, 5)
print('Processando')
sleep(2)
print('-=-' * 20)
if num1 == num2:
    print('Você acertou.... O número é: {}'.format(num2))
else:
    print('Você errou o número é: {}'.format(num2))