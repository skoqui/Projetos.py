dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos Km foram percorridos? "))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar pelo seu aluguel foi de R${:.2f}".format(pago))