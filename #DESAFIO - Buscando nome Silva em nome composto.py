#DESAFIO - Buscando nome Silva em nome composto

nome = str(input("Qual é o sue nome completo? ")).strip()
print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))