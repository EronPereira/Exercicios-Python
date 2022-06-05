# Calculo IPRF
salario = 1
print("Calculo de contribuição IPRF    ///DIGITE 0 PARA SAIR")
while salario > 0:
    salario = float(input("Digite o salário: "))
    if 0 < salario <= 1903.98:
        print('Isento de IPRF')
    elif 1903.99 <= salario <= 2826.65:
        contribuicao = (7.5*salario/100)
        salariof = salario - contribuicao
        print('Contribuição 7.50% = R${}\n'.format(contribuicao))
    elif 2826.66 <= salario <= 3751.05:
        contribuicao = (15*salario/100)
        salariof = salario - contribuicao
        print('Contribuição 15.00% = R${}\n'.format(contribuicao))
    elif 3751.06 <= salario <= 4664.68:
        contribuicao = (22.5*salario/100)
        salariof = salario - contribuicao
        print('Contribuição 22.50% = R${}\n'.format(contribuicao))
    elif 0 < salario >= 4664.69:
        contribuicao = (22.7*salario/100)
        salariof = salario - contribuicao
        print('Contribuição 22.70% = R${}\n'.format(contribuicao))
print("Fim do programa")