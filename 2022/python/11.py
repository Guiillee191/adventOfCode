import math

def parse(lines):
	monkeys=[]
	objects=[]
	testTrue=0
	testFalse=0
	operation=''
	for line in lines:
		splited=line.split()
		if line!='\n':
			if splited[0]=='Starting':
				tmp=line.split(': ')
				tmp2=tmp[1].split(', ')
				for item in tmp2:
					objects.append(int(item))
			elif splited[0]=='Operation:':
				tmp=line.split('= ')
				operation=tmp[1]
			elif splited[0]=='Test:':
				div=int(splited[3])
			elif splited[0]=='If' and splited[1]=='true:':
				testTrue=int(splited[5])
			elif splited[0]=='If' and splited[1]=='false:':
				testFalse=int(splited[5])
		else:
			monkeys.append(Monkey(list(objects), operation, div, testTrue, testFalse))
			objects.clear()
	return monkeys

def starOne(monkeys, rounds, M):
	inspects=[]
	for monkey in monkeys:
		inspects.append(0)
	for i in range(rounds):
		c=0
		for monkey in monkeys:
			for item in monkey.objects:
				inspects[c]+=1
				worryLevel=monkey.operation(item)%M
				monkeys[monkey.nextMonkey(worryLevel)].addItem(worryLevel)
			monkey.objects.clear()
			c+=1
		print('round: ', i, ', ', inspects)
		#for m in monkeys:
		#	m.printMonkey()
		#	print('----------------')
		#print('----------------')
	return inspects


class Monkey:
	def __init__(self, objects, op, divide, testTrue, testFalse):
		self.objects=objects
		self.op=op
		self.testTrue=testTrue
		self.testFalse=testFalse
		self.divide=divide
	def operation(self, old):
		return eval(self.op)
	def nextMonkey(self, current):
		if current%self.divide==0:
			return self.testTrue
		else:
			return self.testFalse
	def addItem(self, item):
		self.objects.append(item)
	def printMonkey(self):
		print('items: ', self.objects)
		print('op: ', self.op, end='')
		print('test: ', self.divide)
		print('testTRue: ', self.testTrue, 'testFalse: ', self.testFalse)

file1=open('../inputs/input11')
lines=file1.readlines()
monkeys=parse(lines)
M=1
for m in monkeys:
	M*=m.divide
result=starOne(monkeys, 10000, M)
result.sort()
print(result[-1]*result[-2])
file1.close()
