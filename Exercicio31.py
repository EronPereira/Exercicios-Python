#Calculando o preço de uma viagem
km = float(input('Informe a distância de viagem em KM: '))
if km <= 200:
    preco = km * 0.50
    print('A viagem de {:.0f}Km custa R${:.2f}'.format(km, preco))
else:
    preco = km * 0.45
    print('A viagem de {}Km custa R${:.2f}'.format(km, preco))