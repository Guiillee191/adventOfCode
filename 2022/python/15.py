import re
import time

sensorPositions=[]
beaconPositions=[]


#Sensor at x=9, y=16: closest beacon is at x=10, y=16

def parse(lines):
    global sensorPositions
    global beaconPositions

    min_i=0
    min_j=0
    max_i=0
    max_j=0

    for line in lines:
        pattern='-?\d+\.?\d*'
        data=re.findall(pattern, line)
        sensorPositions.append([int(data[0]), int(data[1])])
        beaconPositions.append([int(data[2]), int(data[3])])
        if int(data[1])<min_i:
            min_i=int(data[1])
        if int(data[3])<min_i:
            min_i=int(data[3])
        if int(data[0])<min_j:
            min_j=int(data[0])
        if int(data[2])<min_j:
            min_j=int(data[2])

        if int(data[1])>max_i:
            max_i=int(data[1])
        if int(data[3])>max_i:
            max_i=int(data[3])
        if int(data[2])>max_j:
            max_j=int(data[2])
        if int(data[0])>max_j:
            max_j=int(data[0])

    #print(sensorPositions)
    #print(beaconPositions)
    print('mins: ', min_i, min_j)
    print('maxs: ', max_i, max_j)

    minS=1000000
    minSensor=[]
    minBeacon=[]
    maxS=0
    maxSensor=[]
    maxBeacon=[]

    for s,b in zip(sensorPositions, beaconPositions):
        if s[0]<minS:
            minS=s[0]
            minSensor=s
            minBeacon=b
        if s[0]>maxS:
            maxS=s[0]
            maxSensor=s
            maxBeacon=b
    min_j-=abs(minSensor[1]-minBeacon[1])+abs(minSensor[0]-minBeacon[0]) 
    max_j+=abs(maxSensor[1]-maxBeacon[1])+abs(maxSensor[0]-maxBeacon[0]) 
    

    target=[]
    for i in range(abs(min_j)+max_j+1):
        target.append('.')

    
    for s,b in zip(sensorPositions,beaconPositions):
        s[1]+=abs(min_i)
        s[0]+=abs(min_j)
        b[1]+=abs(min_i)
        b[0]+=abs(min_j)
    
    return target
    

def printMapa(mapa):
    for line in mapa:
        for c in line:
            print(c,end='')
        print('')

def starOne(target):
    y=9
    c=0
    for s,b in zip(sensorPositions, beaconPositions):
        
        #print('checking: ', s)
        distance=abs(s[1]-b[1])+abs(s[0]-b[0])
        #print('distance: ', distance)
        current=list(s)
        while current[1]!=y and distance>0:
            if current[1]<y:
                current[1]+=1
                distance-=1
            elif current[1]>y:
                current[1]-=1
                distance-=1
                #time.sleep(1)

            #print('arrived: ', current, 'remaining: ', distance)
        if distance>0:
            for i in range(int(distance)+1):
                target[current[0]-i]='#'
                target[current[0]+i]='#'
        
        #else:
         #   print(s, ' not')
        #print(target)
        #print('')
        #time.sleep(5)
    for b,s in zip(beaconPositions, sensorPositions):
        if b[1]==y:
            target[b[0]]='B'
        if s[1]==y:
            target[s[0]]='S'
    #print(target)
    for s in target:
        if s=='#':
            c+=1
    print(c)
    return c
            

file1=open('../inputs/input15')
lines=file1.readlines()
target=parse(lines)
print(len(target))
print('')
starOne(target)
