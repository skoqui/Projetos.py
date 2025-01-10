# EXERCICIO DOBRO, TRIPLO E RAIZ

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'.format(n, t))
print('A raiz quadrada de {} vale {:.2f}.'.format(n, r))


n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2))) 
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))



# EXERCICIO MÉDIA ARITIMÉTICA

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) /2
print('A média entre {} e {} é igual a {}.'.format(n1, n2, média))




# EXERCICIO CONVERSOR DE MEDIDAS

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A media de {}m corresponde a {}cm e {}mm.'.format(medida, cm, mm))


# EXERCICIO TABUADA


num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 12)





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





# EXERCICIO PINTANDO PAREDE

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
soma = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, soma))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(soma/2))





# EXERCICIO PORCENTAGEM - DESCONTOS

preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5/100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preco, novo))