print('###Analisador de triângulos###')
tr1 = float(input('Informe o segmento 1: '))
tr2 = float(input('Informe o segmento 2: '))
tr3 = float(input('Informe o segmento 3: '))
cores = {'Verde':'\033[32m', 'Vermelho':'\033[31m'}
if tr1 < tr2 + tr3 and tr2 < tr1 + tr3 and tr3 < tr1 + tr2:
    print('Os segmentos formam um triângulo')
else:
    print('Os segmentos não formam um triângulo')
