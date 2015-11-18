n = int(input("Informe um numero: "))

def n_n(n):
	if n==0:
		print ("Numero e igual zero")
	else:
		for i in range(1,n+1):
			print(i)
n_n(n)