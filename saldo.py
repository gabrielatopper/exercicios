numero_conta = int(input("Iforme o numero da conta: "))
print(numero_conta)
saldo = float (input("Informe o saldo: "))
print (saldo)
debito = float (input ("Informe o debito: "))
print(debito)
credito = float (input("Informe o credito: "))
print(credito)
saldo_atual = ((saldo - debito) + credito)
if saldo_atual>= 0:
	print("Saldo Positivo")
else:
	print("Saldo Negativo")