# Pintando a parede
n1 = float(input('Digite a largura da parede:'))
n2 = float(input('Digite a altura da parede:'))
area = n1 * n2
tinta = area / 2
print('Sua parede de dimensão {} x {} possui uma área de: {}m²'.format(n1, n2, area))
print('Para pintar uma parede com área de {} são necessários {}L de tinta'.format(area, tinta))
