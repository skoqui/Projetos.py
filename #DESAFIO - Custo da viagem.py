#DESAFIO - Custo da viagem

distancia = float(input('Qual a distância percorrida? '))

if distancia <= 200:
    cobranca = distancia * 0.50
else:
    cobranca = distancia * 0.45
    
print(f'O custo da viagem será de R${cobranca:.2f} reais')