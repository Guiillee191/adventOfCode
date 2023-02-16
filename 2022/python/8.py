def starOne(mapa):
	width=len(mapa[0])-1
	height=len(mapa)-1
	c=0
	for i in range(1,height):
		for j in range(1,width):
			if visible(mapa, i, j):
				#print('FOUND')
				c+=1
	return c + 2*width + 2*height

def starTwo(mapa):
	width=len(mapa[0])-1
	height=len(mapa)-1
	maxim=0
	for i in range(1,height):
		for j in range(1,width):
			tmp=score(mapa, i, j)
			if tmp>maxim:
				maxim=tmp


	return maxim


def visible(mapa, i, j):
	width=len(mapa[0])
	height=len(mapa)
	top=False
	bottom=False
	left=False
	right=False
	
	#print('start: ', i, j)
	for k in range(j):
		#print(i, k)
		if mapa[i][j]<=mapa[i][k]:
			left=True
		#	print('left found')
			break
	
	for k in range(i):
		#print(k, j)
		if mapa[i][j]<=mapa[k][j]:
			top=True
		#	print('top found')
			break
	
	for k in range(j+1,width):
		#print(i, k)
		if mapa[i][j]<=mapa[i][k]:
			right=True
		#	print('right found')
			break
	
	for k in range(i+1,height):
		#print(k, j)
		if mapa[i][j]<=mapa[k][j]:
			bottom=True
		#	print('bottom found')
			break
			
	return not (top and left and bottom and right)

def score(mapa, i, j):
	width=len(mapa[0])
	height=len(mapa)
	top=0
	bottom=0
	left=0
	right=0
	
	k=j-1
	#print('start: ', i, j, 'val: ', mapa[i][j])
	while k>=0:
		left+=1
		#print('left: ', i, k, ': ', left)
		if mapa[i][j]<=mapa[i][k]:
			
		#	print('left found')
			break
		k-=1
	
	k=i-1
	while k>=0:
		top+=1
		#print('top: ', k, j, ': ', top)
		if mapa[i][j]<=mapa[k][j]:
			
		#	print('top found')
			break
		k-=1
	
	for k in range(j+1,width):
		
		right+=1
		#print('rigth: ', i, k, ': ', right)
		if mapa[i][j]<=mapa[i][k]:
			
		#	print('right found')
			break
		
	
	for k in range(i+1,height):
		
		bottom+=1
		#print('bottom: ', k, j, ': ', bottom)
		if mapa[i][j]<=mapa[k][j]:
			
		#	print('bottom found')
			break
		
			
	return top*left*bottom*right


file1=open('../inputs/input8')
lines=file1.readlines()
mapa=[]
for line in lines:
	mapa.append(line.replace('\n', ''))
print(starOne(mapa))
print(starTwo(mapa))
file1.close()
