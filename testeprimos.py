 # -*- coding:latin1 -*-
def teste1_100(num):
	n = num
	if not(n==2) and (n%2==0):
		return False
	else:
		return True

for i in range(1,100):
	print (teste1_100(i))


for i in range(333,210,-1):
	print ("__________________")
	print (i)
	print (teste1_100(i))