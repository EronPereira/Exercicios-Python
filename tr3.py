#Calculo IPRF
salario = 1
contribuicaoinss = 0
print("Calculo IPRF   ///Digite 0 para sair")
while salario > 0:
    salario = float(input("Digite seu salário: R$"))
#INSS
    if 0 < salario <= 1100.00:
        contribuicaoinss = (7.5*salario)/100
        print('Contribuição INSS a descontar do salário= R${}'.format(contribuicaoinss))
    elif 1100.01 <= salario <= 2203.48:
        contribuicaoinss = (9.0*salario/100)
        print('Contribuição INSS a descontar do salário= R${}'.format(contribuicaoinss))
    elif 2203.49 <= salario <= 3305.22:
        contribuicaoinss = (12*salario/100)
        print('Contribuição INSS a descontar do salário= R${}'.format(contribuicaoinss))
    elif 0 < salario >= 3305.23:
        contribuicaoinss = (14*salario/100)
        print('Contribuição INSS a descontar do salário= R${}'.format(contribuicaoinss))
#IPRF
    if 0 < salario <= 1903.98:
        print('Isento de IPRF')
    elif 1903.99 <= salario <= 2826.65:
        calculop = ((salario - contribuicaoinss) * 7.5) / 100
        calculof = calculop - 142.80
        print('Aliquota de 7.50% aplicada sobre o salário = R${}\nValor deduzido = R$142.80\nValor a pagar = R${}'.format(calculop, calculof))
        print("[(R$" + '{} - {}'.format(salario, contribuicaoinss) + ") X 7.5.%]" + ' - R$636.13 = R${}\n'.format(calculof))
    elif 2826.66 <= salario <= 3751.05:
        calculop = ((salario - contribuicaoinss) * 15) / 100
        calculof = calculop - 354.80
        print('Aliquota de 15.00% aplicada sobre o salário = R${}\nValor deduzido = R$354.80\nValor a pagar = R${}'.format(calculop,calculof))
        print("[(R$" + '{} - {}'.format(salario, contribuicaoinss) + ") X 15%]" + ' - R$636.13 = R${}\n'.format(calculof))
    elif 3751.06 <= salario <= 4664.68:
        calculop = ((salario - contribuicaoinss)* 22.5)/100
        calculof = calculop - 636.13
        print('Aliquota de 22.50% aplicada sobre o salário = R${}\nValor deduzido = R$636.13\nValor a pagar = R${}'.format(calculop, calculof))
        print("[(R$"+'{} - {}'.format(salario, contribuicaoinss)+") X 22.5%]"+' - R$636.13 = R${}\n'.format(calculof))
    elif 0 < salario >= 4664.69:
        calculop = ((salario - contribuicaoinss) * 27.5) / 100
        calculof = calculop - 869.36
        print('Aliquota de 27.50% aplicada sobre o salário = R${}\nValor deduzido = R$869.36\nValor a pagar = R${}'.format(calculop, calculof))
        print("[(R$" + '{} - {}'.format(salario, contribuicaoinss) + ") X 27.5%]" + ' - R$636.13 = R${}\n'.format(calculof))
print("Fim do programa")