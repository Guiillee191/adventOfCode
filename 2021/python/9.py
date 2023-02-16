def starOneBetter(mapa):
	riskLvl=0
	for i in range(1, len(mapa)-1):
		for j in range(1, len(mapa[0])-1):
			if checkLowest(mapa,i,j):
				riskLvl+=(int(mapa[i][j])+1)

	return riskLvl

def starTwo(mapa):
	sizes=[]
	for i in range(1, len(mapa)-1):
		for j in range(1, len(mapa[0])-1):
			if checkLowest(mapa,i,j):
				sizes.append(searchBasin(i,j,mapa))
	sizes.sort()
	sizes.reverse()
	
	return sizes[0]*sizes[1]*sizes[2]

def checkLowest(mapa, i,j):
	if mapa[i][j]<mapa[i+1][j] and mapa[i][j]<mapa[i][j+1] and mapa[i][j]<mapa[i-1][j] and mapa[i][j]<mapa[i][j-1]:
		return True
	return False

def searchBasin(i,j,mapa):
	val=0
	if mapa[i][j]=='9':
		return val
	val+=1
	mapa[i]=mapa[i][:j]+'9'+mapa[i][j+1:]
	val+=searchBasin(i+1, j, mapa)
	val+=searchBasin(i, j+1, mapa)
	val+=searchBasin(i-1, j, mapa)
	val+=searchBasin(i, j-1, mapa)
	return val

file1=open('../inputs/input9')
lines=file1.readlines()
mapa=[]
limiter=''
for i in range(len(lines[0])+1):
	limiter+='9'
mapa.append(limiter)
for line in lines:
	mapa.append('9' + line.replace('\n', '9'))
mapa.append(limiter)



war='\033[93m'
endc='\033[0m'

print(starOneBetter(mapa))
print(starTwo(mapa))
file1.close()
