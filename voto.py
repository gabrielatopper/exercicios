# -*- coding:latin1 -*-
ano_atual= int (input("Informe o ano atual: "))
print(ano_atual)
ano_nasc = int(input("Informe o seu ano de nascimento: "))
print (ano_nasc)
idade = (ano_atual-ano_nasc)
if idade >= 16:
	print ("Voce pode votar")
else:
	print ("Voce nao pode votar")