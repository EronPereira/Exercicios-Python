v1 = input('Digite algo:')
print('Possui espaço?', v1.isspace())
print('È alfanúmerico?', v1.isalnum())
print('É um número?', v1.isnumeric())
print('É alfabético?', v1.isalpha())
print('Esta em maiuscula?', v1.isupper())
print('Esta em minuscula?', v1.islower())
print('Esta capitalizada?', v1.istitle())

print('Possui espaço? {}'.format(v1.isspace()))