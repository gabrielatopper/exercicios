qtd_atual = int (input("Informe a quantidade atual em estoque: "))
print(qtd_atual)
qtd_maxima = int (input("Informe a quantidade maxima em estoque: "))
print(qtd_maxima)
qtd_minima = int (input("Informe a quantidade minima em estoque: "))
print(qtd_minima)
qtd_media = ((qtd_maxima + qtd_minima)/2)
print(qtd_media)
if qtd_atual >= qtd_media:
	print("Nao efetuar compra")
else:
	print("Efetuar compra")