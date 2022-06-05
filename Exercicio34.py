print('###Aumento de salário###')
salario = float(input('Informe o valor do salário do funcionário: R$'))
if salario > 1250:
    salariofn = salario + (salario * 10 / 100)
else:
    salariofn = salario + (salario * 15 / 100)
print('O valor do salário será de RS{:.2f}'.format(salariofn))