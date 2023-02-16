


def starOne(fileName):
	file1 = open(fileName)
	max = 0
	suma = 0
	lines = file1.readlines()
	
	for line in lines:
		if line == '\n':
			if max < suma:
				max = suma
			suma = 0
		else:
			  suma += int(line)

	print(max)
	file1.close()

def starTwo(fileName):
	file1 = open(fileName)
	listaMaximos = []
	suma = 0
	lines = file1.readlines()
	
	for line in lines:
		if line == '\n':
			listaMaximos.append(suma)
			suma = 0
		else:
			  suma += int(line)
	
	listaMaximos.sort()
	listaMaximos.reverse()
	resultado = 0
	
	for i in range(3):
		resultado += listaMaximos[i]
	
	print(resultado)
	file1.close()
		
#starOne('test')
starTwo('input1')


