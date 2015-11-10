
horas_trab = int(input("Informe o numero de horas trabalhadas em mês: "))
print (horas_trab)
salario_hora = int(input("informe o valor do salario por hora: "))
print(salario_hora)



## hahahahaha
print ("guerrerira selvagem")

def soma_selvagem(num1,num2):
	resultado = num1+num2
	return resultado
soma_selvagem (2,2)

def selvagem (num1,num2):
        resultado = num1*num2
        return resultado
selvagem (8,8)

def tabuada (num):
	for multiplicador in range (0,11):
		print (multiplicador*num)

num= int(input("Informe um numero: "))
tabuada (num)

def tabuada1 ():
	for multiplicado in range (1,11):
		print ("Tabuada do: ", multiplicado)
		for multiplicador in range (0,11):
			print (multiplicador, " x ", multiplicado, " = ",  multiplicador*multiplicado)
		print ("________________________________")
tabuada1()