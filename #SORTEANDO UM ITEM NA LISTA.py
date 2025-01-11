#SORTEANDO UM ITEM NA LISTA

'''import random 

lista = ["Pedro", "Maria", "João", "Rafael"]

print("Primeiro aluno: {}".format(random.choice(lista)))
print("Segundo aluno: {}".format(random.choice(lista)))
print("Terceiro aluno: {}".format(random.choice(lista)))
'''

from random import choice

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista = [a1, a2, a3, a4]

print("O aluno escolhido foi: {}".format(choice(lista)))