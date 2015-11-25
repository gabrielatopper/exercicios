total_estoque = 0
media = 0
valor_mercadorias = int (input("Informe o valor de cada mercadoria: "))

for i in range (1, +1):
	num_mercadorias = int (input("Informe o total de mercadorias:"))
	print (num_mercadorias)
total_estoque = total_estoque + valor_mercadorias
media = total_estoque / num_mercadorias
print(media)