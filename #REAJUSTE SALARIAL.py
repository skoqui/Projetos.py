

salario = int(input("Qual o salário do funcionário: R$"))
valor = salario + (salario * 15 / 100)
print("O salário com 15% de aumento é: R${:.2f}".format(valor))
