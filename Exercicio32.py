print('Verificando se o ano é bissexto...')
n = int(input('Digite 1 para verificar o ano atual ou digite 2 para informar um ano: '))
if n == 2:
    ano = int(input('Informe o ano para ser veríficado: '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano de {} é Bissexto'.format(ano))
    else:
        print('O ano de {} não é Bissexto'.format(ano))
else:
    from datetime import date
    ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano de {} é Bissexto'.format(ano))
    else:
        print('O ano de {} não é Bissexto'.format(ano))