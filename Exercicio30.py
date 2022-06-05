print('-=-' * 20 + '\nVerificando se o número é ímpar ou par...\n' + '-=-' * 20)
num = int(input('\nDigite um número: '))
resultado = num % 2
print('\n'+'-=-' * 20)
if resultado == 0:
    print('O número é Par')
else:
    print('O número é ímpar')