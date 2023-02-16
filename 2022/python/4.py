def starOne(data):
	c=0
	for f in data:

		if set(f[0])==(set(f[0])&set(f[1])) or set(f[1])==(set(f[0])&set(f[1])):
				c+=1
				print(f)
	return c

def starTwo(data):
	c=0
	for f in data:

		if len(set(f[0])&set(f[1]))!=0:
				c+=1

	return c


file1=open('../inputs/input4')
lines=file1.readlines()
data=[]
for line in lines:
	split1=line.split(',')
	e=[]
	for s in split1:
		split2=s.split('-')
		lista=[]

		for j in range(int(split2[0]), int(split2[1])+1):
			lista.append(j)
		e.append(lista)

	data.append(e)

file1.close()

#print(starOne(data))
print(starTwo(data))
