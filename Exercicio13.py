# Reajuste salárial
salario = float(input('Qual o salário do funcionário? R$'))
reajuste = salario + (salario * 15 / 100)
print('O salário de R${:.2f} com reajuste de 15% fica R${:.2f}'.format(salario, reajuste))
