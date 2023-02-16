

def parse(lines):
	moves=[]
	for line in lines:
		tmp=line.split()
		moves.append([tmp[0], tmp[1]])
	return moves

def starOne(moves):
	grid=[]
	visited=[]
	
	for i in range(10):
		grid.append([])
		viisited.append([])
		for j in range(10):
			grid[i].append('.')
			visited[i].append(False)
	grid[len(grid)][0]='H'
	visited[len(grid)][0]=True
	headPos=[len(grid),0]
	tailPos=[len(grid),0]
	for move in moves:
		if move[0]=='R':
			for i in range(int(move[2])):
				headPos[1]+=1
				o=checkDistance(headPosition, tailPosition)
				if o==1:
					
				elif o==2:
					
				visited[][]
		elif move[0]=='U':
			for i in range(int(move[2])):
				headPos[0]-=1
				o=checkDistance(headPosition, tailPosition)
				if o==1:
				
				elif o==2:
					
					
				visited[][]
		elif move[0]=='D':
			for i in range(int(move[2])):
				headPos[0]+=1
				o=checkDistance(headPosition, tailPosition)
				if o==1:
				
				elif o==2:
					
					
				visited[][]
		elif move[0]=='L':
			for i in range(int(move[2])):
				headPos[1]-=1
				o=checkDistance(headPosition, tailPosition)
				if o==1:
				
				elif o==2:
					
					
				visited[][]

def checkDistance(head, tail):
	 if (head[0]==tail[0] or head[1]==tail[1]) and abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1:
	 	return 1
	 elif abs(head[0]-tail[0])>2 or abs(head[1]-tail[1])>2:
	 	return 2
	 else:
	 	return 0
	 
		
file1=open('../inputs/test')
moves=parse(file1.readlines())
starOne(moves)
file1.close()
