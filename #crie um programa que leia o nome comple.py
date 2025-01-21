#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas
#o nome com todas as letras minusculas
#quantas letras ao todo(sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper())) 
print('Seu nome em minúsculas é {}'.format(nome.lower()))
nome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome[0], len(nome[0])))
print('Seu nome completo tem {} letras'.format(len(''.join(nome))))