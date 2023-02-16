def starOne(stream):
	for i in range(4,len(stream)):
		current=stream[i-4:i]
		if len(set(current))==len(current):
			print(i, current)
			break
def starTwo(stream):
	for i in range(14,len(stream)):
		current=stream[i-14:i]
		if len(set(current))==len(current):
			print(i, current)
			break


file1=open('../inputs/input6')
lines=file1.readlines()
stream=lines[0]
starOne(stream)
starTwo(stream)
