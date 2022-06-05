# Catetos e Hipotenusa
from math import pow, sqrt, hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
#hipo = sqrt(pow(co, 2) + pow(ca, 2)) # math.hypot(co, ca)
hipo = hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(hipo))
