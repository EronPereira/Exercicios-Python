print('======Radar Eletrônico======')
km = float(input('Qual a velocidade do veículo: '))
if km >= 80:
    multa = (km - 80) * 7.00
    print('O veículo foi multado. O valor da multa é: R${:.2f}'.format(multa))
else:
    print('O veículo está dentro do limite de velocidade')