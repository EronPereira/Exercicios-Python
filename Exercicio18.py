# Seno, Cosseno  e Tangente
from math import sin, cos, tan, radians
num = float(input('Digite o valor do ângulo:'))
print('Seno: {:.2f}º\nCosseno: {:.2f}º\nTangente: {:.2f}º'.format(sin(radians(num)), cos(radians(num)), tan(radians(num))))
