# EXERCICIO PINTANDO PAREDE

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
soma = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, soma))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(soma/2))

