

def starOne(initialState, days):
	next=nextState(initialState)
	for i in range(days-1):
		#print(i)
		next=nextState(next, 1)
	return next
		
def starOneFast(initialState, days):

	i=6
	step=6
	next=nextState(initialState, step)
	while i<days:
		tmp=min(step, days-i)
		print(i)
		next=nextState(next, tmp)
		i+=tmp
	return next

def nextState(state, step):
	#next=list(state)
	for fish in range(len(state)):
			state[fish]-=step
			if state[fish] < 0:
				state.append((9+state[fish]))
				state[fish]+=7
	return state
	
def starOneFastV2(initialState, days):
	#comprimir
	state=compress(initialState)
	
	#iterar
	next=iterate(state)
	for i in range(days-1):
		next=iterate(next)
	suma=0
	for s in next:
		suma+=s[1]
	return suma

def compress(state):
	compressState=[]
	for i in range(9):
		compressState.append([i, 0])

	for val in state:
		compressState[val][1]+=1

	return compressState

def iterate(state):
	tmp=state[0][1]
	for i in range(0,8):
		state[i][1]=state[i+1][1]
	state[6][1]+=tmp
	state[8][1]=tmp
	return state

data=[]
file1=open('../inputs/input6')
lines=file1.readlines()
dataS=lines[0].split(',')
data=[]
for d in dataS:
	data.append(int(d))
print(starOneFastV2(data, 256))
