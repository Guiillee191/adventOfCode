

def starOne(fileName):
	posHorizontal=0
	depth=0
	
	file1=open(fileName)
	lines=file1.readlines()
	for line in lines:
		tmp=line.split()
		if tmp[0] == 'forward':
			posHorizontal+=int(tmp[1])
		if tmp[0] == 'down':
			depth+=int(tmp[1])
		if tmp[0] == 'up':
			depth-=int(tmp[1])

	print(depth*posHorizontal)
	file1.close()

def starTwo(fileName):
	posHorizontal=0
	depth=0
	aim=0
	
	file1=open(fileName)
	lines=file1.readlines()
	for line in lines:
		tmp=line.split()
		if tmp[0] == 'forward':
			posHorizontal+=int(tmp[1])
			depth+=aim*int(tmp[1])
		if tmp[0] == 'down':
			aim+=int(tmp[1])
		if tmp[0] == 'up':
			aim-=int(tmp[1])
	print(depth*posHorizontal)
	file1.close()
	
starOne('../inputs/input2')
starTwo('../inputs/input2')
