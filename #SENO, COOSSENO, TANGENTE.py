#SENO, COOSSENO, TANGENTE

import math 

angulo = float(input("Digite o angulo: "))

seno = math.sin(math.radians(angulo))
print(f"Seno: {seno:.2f}")

cosseno = math.cos(math.radians(angulo))
print(f"Cosseno: {cosseno:.2f}")

tangente = math.tan(math.radians(angulo))
print(f"Tangente: {tangente:.2f}")