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


--------------------------------------------------------------------------------------










#TRABALHANDO COM IMPORTS

from math import sqrt

num = int(input('Digite um número: '))
raiz = math.sqrt(num)


#CEIL = Arredonda pra cima
#Floor = Arredonda para baixo





import random
num = random.randint(1, 10)
print(num)



import emoji
print(emoji.emojize("Olá, Mundo :sunglasses:", use_aliases=True))




#quebrando um número para inteiro
from math import trunc

num = float(input("Digite um número: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))


''' OU SEM IMPORT '''

num = float(input("Digite um número: "))
print("O valor digitado {} e a sua porção inteira é {}".format(num, int(num)))




#CATETOS E HIPOTENUSA
import math
 
com = float(input("Digite o comprimento do cateto oposto: "))
adj = float(input("Digite o comprimento do cateto adjacente: "))
hip = math.hypot(com, adj)
print("A hipotenusa vai medir {:.2f}".format(hip))  


''' MODO 2 '''

from math import hypot
com = float(input("Digite o comprimento do cateto oposto: "))
adj = float(input("Digite o comprimento do cateto adjacente: "))
hip = hypot(com, adj)
print("A hipotenusa vai medir {:.2f}".format(hip))


#SENO, COOSSENO, TANGENTE

import math 

angulo = float(input("Digite o angulo: "))

seno = math.sin(math.radians(angulo))
print(f"Seno: {seno:.2f}")

cosseno = math.cos(math.radians(angulo))
print(f"Cosseno: {cosseno:.2f}")

tangente = math.tan(math.radians(angulo))
print(f"Tangente: {tangente:.2f}")


#SORTEANDO UM ITEM NA LISTA

import random 

lista = ["Pedro", "Maria", "João", "Rafael"]

print("Primeiro aluno: {}".format(random.choice(lista)))
print("Segundo aluno: {}".format(random.choice(lista)))
print("Terceiro aluno: {}".format(random.choice(lista)))


''' ou '''

from random import choice

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista = [a1, a2, a3, a4]

print("O aluno escolhido foi: {}".format(choice(lista)))




lens() #Faz com que a função retorne o tamanho da string	 exemplo: len('Olá mundo') retorna 9
count() #Faz com que a função retorne quantas vezes um determinado caractere aparece na string 		exemplo: 'Olá mundo'.count('o') retorna 2
upper() #Faz com que a função retorne a string em letras maiúsculas 	exemplo: 'Olá mundo'.upper() retorna 'OLÁ MUNDO'
lower() #Faz com que a função retorne a string em letras minúsculas 	exemplo: 'Olá mundo'.lower() retorna 'olá mundo'
strip() #Faz com que a função retorne a string sem espaços em branco no início e no final 	exemplo: '   Olá mundo   '.strip() retorna 'Olá mundo'
replace() #Faz com que a função retorne a string com um determinado caractere substituído por outro 	exemplo: 'Olá mundo'.replace('o', 'a') retorna 'Alá mundo'
split() #Faz com que a função retorne uma lista dividida por um determinado caractere 	exemplo: 'Olá mundo'.split(' ') retorna ['Olá', 'mundo']
join() #Faz com que a função retorne uma string unida por um determinado caractere 	exemplo: ''.join(['Olá', 'mundo']) retorna 'Olámundo'
