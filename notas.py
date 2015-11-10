# -*- coding: latin1 -*-
n1= float(input("Informe a primera nota: "))
print (n1)
n2 = float(input("Informe a segunda nota: "))
print (n2)
media = n1+n2/2
if media >=6:
	print("Aluno Aprovado")
else:
	print ("Aluno Reprovado")
print ("A media e:", media)