#DESAFIO - A cidade precisa começar com a palavra SANTO


cidade = str(input("Em que cidade você nasceu? ")).strip()
print(cidade[:5].upper() == "SANTO")
print(cidade.upper())