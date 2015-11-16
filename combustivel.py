litros = int(input("Informe o numero de litros vendidos: ")) 
print(litros)
t_combust = raw_input("A para alcool, G para gasolina: ")
print(t_combust)
preco_alcool = 2.90
preco_gasolina = 3.30
if t_combust == "A" :
	if litros<20: 
		preco_total=preco_alcool*litros 
		print(preco_total-preco_total*0.03)
	else:
		preco_total=preco_gasolina*litros
		print(preco_total-preco_total*0.04)
else:
	if litros<20: 
		preco_total=preco_alcool*litros 
		print(preco_total-preco_total*0.05)
	else:
		preco_total=preco_gasolina*litros
		print(preco_total-preco_total*0.06)