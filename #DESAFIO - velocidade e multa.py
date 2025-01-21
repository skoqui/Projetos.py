#DESAFIO - velocidade e multa


km = int(input('Qual é a sua velocidade? '))
v = 80
m =  7

if km <= v:
    print(f'Você está dirigindo a uma velocidade de {km}km/h. Cuidado com o limite de velocidade acima de 80km/h.')
else:
    excesso = km - v
    multa = excesso * m 
    print(f'Você excedeu o limite de velocidade de 80km/h em {excesso}km/h e sua multa será de R${multa:.2f} reais.')
    