# Calculo INSS
salario = 1
print("Calculo de contribuição INSS   ///Digite 0 para sair")
while salario > 0:
    salario = float(input("Digite o salário: "))
    if salario <= 1100.00:
        contribuicao = (7.5*salario)/100
        salariof = salario - contribuicao
        print('Contribuição 7.50% = R${}\nSeu salário final será: R${:.2f}\n'.format(contribuicao, salariof))
    elif 1100.01 <= salario <= 2203.48:
        contribuicao = (9.0*salario/100)
        salariof = salario - contribuicao
        print('Contribuição 9.00% = R${}\nSeu salário final será: R${:.2f}\n'.format(contribuicao, salariof))
    elif 2203.49 <= salario <= 3305.22:
        contribuicao = (12*salario/100)
        salariof = salario - contribuicao
        print('Contribuição 12.00% = R${}\nSeu salário final será: R${:.2f}\n'.format(contribuicao, salariof))
    elif 0 < salario >= 3305.23:
        contribuicao = (14*salario/100)
        salariof = salario - contribuicao
        print('Contribuição 14.00% = R${}\nSeu salário final será: R${:.2f}\n'.format(contribuicao, salariof))
print("Fim do programa")