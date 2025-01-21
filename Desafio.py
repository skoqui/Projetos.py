#faça um numero que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

digite = int(input('Digite um numero de 0 a 9999: '))
u = digite // 1 % 10
d = digite // 10 % 10
c = digite // 100 % 10
m = digite // 1000 % 10
print('Analisando o numero {}'.format(digite))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))