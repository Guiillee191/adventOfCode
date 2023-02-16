import math

def starOne(data):
	suma=0
	priorities={}
	for i in range(1, 27):
		priorities[chr(i+96)]=i
		priorities[chr(i+64)]=i+26
	for d in data:
		split=math.floor((len(d)-1)/2)

		result=set(d[:split])&set(d[split:])
	
		for k in result:
			suma+=priorities[k]
	return suma
			
def starTwo(data):
	suma=0
	priorities={}
	for i in range(1, 27):
		priorities[chr(i+96)]=i
		priorities[chr(i+64)]=i+26
	j=0
	while j<len(data)-2:
		result=set(data[j])&set(data[j+1])&set(data[j+2])
		for k in result:
			suma+=priorities[k]
		j+=3
	return suma

file1=open('../inputs/input3')
lines=file1.readlines()
data=[]
for l in lines:
	data.append(l.replace('\n', ''))

print(starOne(data))
print(starTwo(data))
