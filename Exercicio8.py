#Conversor Metro para Centimetros e Milimetros
n1 = float(input('Digite o tamanho:'))
cm = n1 * 100
mm = cm * 10
print('A medida de {}M corresponde a {:.2f} em Cm e {:.2f} em mm'.format(n1, cm, mm))
