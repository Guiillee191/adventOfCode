

def starOne(data):
	outcomes = {('A','X'):4,('A','Y'):8,('A','Z'):3,('B','X'):1,('B','Y'):5,('B','Z'):9,('C','X'):7,('C','Y'):2,('C','Z'):6}
	puntuation=0
	for play in data:
		puntuation+=outcomes.get(tuple(play))
	print(puntuation)

def starTwo(data):
	puntuation=0
	outcomes = {('A','X'):3,('A','Y'):4,('A','Z'):8,('B','X'):1,('B','Y'):5,('B','Z'):9,('C','X'):2,('C','Y'):6,('C','Z'):7}
	for play in data:
		puntuation+=outcomes.get(tuple(play))
	print(puntuation)

file1=open('../inputs/test')
lines=file1.readlines()
data=[]
for line in lines:
	data.append(line.split())

starOne(data)
starTwo(data)
