def starOne(instructions):
	register=1
	cycle=1
	out=0
	for instruction in instructions:
		split=instruction.split()
		if split[0]=='noop':
			if cycle==20 or cycle==60 or cycle==100 or cycle==140 or cycle==180 or cycle==220:
				out+=cycle*register
			cycle+=1
		elif split[0]=='addx':
			if cycle==20 or cycle==60 or cycle==100 or cycle==140 or cycle==180 or cycle==220:
				out+=cycle*register
			cycle+=1
			if cycle==20 or cycle==60 or cycle==100 or cycle==140 or cycle==180 or cycle==220:
				out+=cycle*register
			cycle+=1
			register+=int(split[1])
	return out

def starOne2(data):
	cycle=0
	register=1
	start=0
	out=0
	for i in range(len(data)):
		while not freeCPU(data[i].split(), start, cycle):
			cycle+=1
			if cycle==20 or ((cycle-20)>=40 and (cycle-20)%40==0):
				out+=register*cycle
		start=cycle
		register+=cpu(data[i].split())
		cycle+=1
		if cycle==20 or ((cycle-20)>=40 and (cycle-20)%40==0):
				out+=register*cycle
	return out


def starTwo(data):
	cycle=0
	register=1
	start=0
	screen=[]
	for j in range(6):
		screen.append([])
		for k in range(40):
			screen[j].append('.')
	#renderScreen(screen)
	for i in range(len(data)):
		while not freeCPU(data[i].split(), start, cycle):
			crt(screen, register, cycle)
			cycle+=1
		
		start=cycle
		register+=cpu(data[i].split())
		crt(screen, register, cycle)
		cycle+=1
		#renderScreen(screen)
	return screen

def cpu(instruction):
	if instruction[0]=='addx':
		return int(instruction[1])
	return 0

def crt(screen, register, cycle):
	screenPointer=[int(cycle/40), cycle%40]

	if screenPointer[1]==register or screenPointer[1]==register-1 or screenPointer[1]==register+1:
		screen[screenPointer[0]][screenPointer[1]]='#'

def freeCPU(instruction, start, cycle):
	if instruction[0]=='addx' and cycle-start<2:
		return False
	else:
		return True

def renderScreen(screen):	
	print('')
	for l in screen:
		for m in l:
			print(m, end='')
		print()
	
file1=open('../inputs/input10')
lines=file1.readlines()
print(starOne(lines))
print(starOne2(lines))
#starTwo(lines)
file1.close()
