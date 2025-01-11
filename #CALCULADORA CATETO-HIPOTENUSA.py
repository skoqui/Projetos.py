#CATETOS E HIPOTENUSA
'''
import math

 
com = float(input("Digite o comprimento do cateto oposto: "))
adj = float(input("Digite o comprimento do cateto adjacente: "))
hip = math.hypot(com, adj)
print("A hipotenusa vai medir {:.2f}".format(hip))  '''



from math import hypot
com = float(input("Digite o comprimento do cateto oposto: "))
adj = float(input("Digite o comprimento do cateto adjacente: "))
hip = hypot(com, adj)
print("A hipotenusa vai medir {:.2f}".format(hip))