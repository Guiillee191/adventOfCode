def starOne(crates, steps):
	for step in steps:
		for i in range(int(step[0])):
			a=int(step[1])-1
			b=int(step[2])-1
			tmp=crates[a][0]
			crates[a].pop(0)
			crates[b].insert(0,tmp)
		print(crates)
	sol=''
	for crate in crates:
		sol+=crate[0]
	return sol
def starTwo(crates, steps):
	for step in steps:
		moved=[]
		for i in range(int(step[0])):
			a=int(step[1])-1
			b=int(step[2])-1
			tmp=crates[a][0]
			crates[a].pop(0)
			moved.append(tmp)
		print(moved)
		moved.reverse()
		for c in moved:
			crates[b].insert(0,c)
		print(crates)
	sol=''
	for crate in crates:
		sol+=crate[0]
	return sol


file1=open('../inputs/input5')
lines=file1.readlines()
crates=[]
steps=[]
size=0
end=0
for i in range(len(lines)):
	if lines[i]=='\n':
		size=len(lines[i-1])
		end=i-1
		for j in range(len(lines[i-1].split())):
			crates.append([])
		break
print(end)
d=0
for line in lines:
	k=1
	c=0
	
	if d<=end:
		k=1
		c=0
		while k<len(line):
			if line[k]!=' ':
				crates[c].append(line[k])
			k+=4
			c+=1
	elif d>end and line!='\n': 
		split=line.split()
		steps.append([split[1],split[3],split[5]])
	d+=1
print(crates)
print(steps)
#print(starOne(crates,steps))
print(starTwo(crates, steps))

