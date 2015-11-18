n = 0
soma = 0
numero_alunos = int (input("Informe o numero de alunos: "))
while n <= numero_alunos:
	notas = int (input ("Informe as notas dos alunos"))
	soma = soma + notas
	n=n+1
media = soma/numero_alunos
print(media)