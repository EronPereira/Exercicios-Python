# Aluguel de carros
km = float(input('Kilometragem percorrida:'))
dia = int(input('Quantidade de dias locado:'))
prfi = km * 0.15 + dia * 60
print('O valor do aluguel custou R${:.2f}'.format(prfi))
