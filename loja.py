total_valor = 0
media = 0
num_mercadorias = int (raw_input("Informe o total de mercadorias:"))

for i in range (0, num_mercadorias):
	valor_mercadorias = int (raw_input("Informe o valor de cada mercadoria: "))
	total_valor = total_valor + valor_mercadorias

print (num_mercadorias)
media = total_valor / num_mercadorias
print (total_valor)
print(media)
