
# EXERCICIO CONVERSOR DE MOEDAS

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 6.29
print('Com R$ {:.2f} você pode comprar U${:.2f}'.format(real, dolar))


real = float(input('Digite o valor de conversão de moeda REAL/DOLAR: R$'))
dolar = real * 6.29
print('O {:.2f} está valendo {:.2f} atualmente'.format(real, dolar))


real = float(input('Digite o valor de conversão de moeda REAL/DOLAR: R$'))
dolar = real * 6.29
print('{:.2f} reais está valendo {:.2f} dólares atualmente'.format(real, dolar))


dolar = float(input('Conversor de DÓLAR para REAL: $'))
real = dolar * 6.29
print('{:.2f} dólares está valendo {:.2f} reais atualmente'.format(dolar, real))
