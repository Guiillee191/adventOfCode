

def starOne(data, mode):
	totalFuel=0
	minFuel=1000000000
	pos=0
	for i in range(min(data), max(data)):
		for h in data:
			if h<i:
				if mode==1:
					totalFuel+=serie(i-h)
				else:
					totalFuel+=(i-h)
			elif h>i:
				if mode==1:
					totalFuel+=serie(h-i)
				else:
					totalFuel+=(h-i)
		if totalFuel<minFuel:
			minFuel=totalFuel
			pos=h
		totalFuel=0
	return minFuel

def serie(a):
	return (a*(a+1))/2

	#if a==1:
	#	return 1
	#return a+serie(a-1)



file1=open("../inputs/input7")
lines=file1.readlines()
data=[]
for i in lines[0].split(','):
	data.append(int(i))
file1.close()
print(starOne(data, 1))
