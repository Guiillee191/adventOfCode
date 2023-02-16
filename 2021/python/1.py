

def starOne(fileName):
	previousLine=10000000000
	file1=open(fileName)
	lines=file1.readlines()
	depth=0
	
	for line in lines:
		if int(line)>previousLine:
			depth+=1;
		previousLine=int(line)
	print(depth)
	file1.close()
	
def starTwo(fileName):
	file1=open(fileName)
	lines=file1.readlines()
	depths=[]
	depthCounter=0
	previousWindow=100000000
	
	for line in lines:
		depths.append(int(line))
	for i in range(len(depths)-2):
		window=depths[i]+depths[i+1]+depths[i+2]
		if previousWindow<window:
			depthCounter+=1
		previousWindow=window
	print(depthCounter)
	file1.close()
	
starOne('../inputs/input1')
starTwo('../inputs/input1')
