def starOne(data, steps):
	
	for i in range(steps):
		flashes=calculate(data)
		print(data)

def calculate(data):
	for i in range(1,len(data)-1):
		for j in range(1,len(data[0])-1):
			updateValue(mapa, i, j, str(int(data[i][j])+1))
			if data[i][j]=='10':
				flashed(data, i, j)
			
	return 1

def flashed(data, i, j):
	if data[i+1][j]!='X':
		updateValue(mapa, i+1, j, )
	if data[i][j+1]!='X':
		updateValue(mapa, i, j+1)
	if data[i-1][j]!='X':
		updateValue(mapa, i-1, j)
	if data[i][j-1]!='X':
		updateValue(mapa, i, j-1)
	if data[i+1][j+1]!='X':
		updateValue(mapa, i+1, j+1)
	if data[i-1][j-1]!='X':
		updateValue(mapa, i-1, j-1)
	if data[i+1][j-1]!='X':
		updateValue(mapa, i+1, j-1)
	if data[i-1][j+1]!='X':
		updateValue(mapa, i-1, j+1)
	
def updateValue(data, i,j, c):
	data[i]=data[i][:j]+c+data[i][j+1:]

file1=open('../inputs/test')
lines=file1.readlines()
mapa=[]
limiter=''
for i in range(len(lines[0])+1):
	limiter+='X'
mapa.append(limiter)
for line in lines:
	mapa.append('X' + line.replace('\n', 'X'))
mapa.append(limiter)

starOne(mapa, 2)

