# Desconto de 5%
prod = float(input('Digite do preço do produto: R$'))
desconto = (prod * 5 / 100)
prf = prod - desconto
print('O produto com valor de R${} com 5% de desconto é: R${:.2f}'.format(prod, prf))
