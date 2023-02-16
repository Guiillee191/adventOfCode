

def starOne(data):
	ones=0
	zeros=0
	gammaRate=''
	epsilonRate=''
	
	for bit in range(len(data[0])-1):
		for bits in data:
			if bits[bit]=='1':
				ones+=1
			if bits [bit]=='0':
				zeros+=1
		if zeros>ones:
			gammaRate+='0'
		else:
			gammaRate+='1'
		zeros=0
		ones=0
	for i in gammaRate:
		if i=='0':
			epsilonRate+='1'
		else:
			epsilonRate+='0'
	print(int(epsilonRate, 2)*int(gammaRate, 2))

def recursive(data, k, mode):
	ones=0
	zeros=0
	remaining=[]
	
	if len(data)==1:
		return data[0]
	for d in data:
		if d[k]=='1':
			ones+=1
		if d [k]=='0':
			zeros+=1
	if ones<zeros:
		if mode==1:
			keep=1
		else:
			keep=0
	else:
		if mode==1:
			keep=0
		else:
			keep=1
		
	for d in data:
		if d[k]==str(keep):
			remaining.append(d)
	return recursive(remaining, k+1, mode)

def starTwo(data):
	print(int(recursive(data, 0, 0), 2)*int(recursive(data, 0, 1), 2))
	
	
data=[]
file1=open('../inputs/input3')
lines=file1.readlines()
for line in lines:
	data.append(line)
file1.close()
starOne(data)
starTwo(data)
