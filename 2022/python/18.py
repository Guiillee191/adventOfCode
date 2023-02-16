import numpy as np
from collections import deque

def parse(lines):
    data=[]
    for line in lines:
        tmp=[]
        splited=line.split(',')
        tmp.append(int(splited[0]))
        tmp.append(int(splited[1]))
        tmp.append(int(splited[2]))
        data.append(tmp)
    print(data)
    return set(tuple(i) for i in data)

def computeClosest(coord):
    closest=[]
    closest.append([coord[0]+1, coord[1], coord[2]])
    closest.append([coord[0]-1, coord[1], coord[2]])
    closest.append([coord[0], coord[1]+1, coord[2]])
    closest.append([coord[0], coord[1]-1, coord[2]])
    closest.append([coord[0], coord[1], coord[2]+1])
    closest.append([coord[0], coord[1], coord[2]-1])
    return set(tuple(i) for i in closest)


file1=open('../inputs/input18')
lines=file1.readlines()
data=parse(lines)

c=0
for coord in data:
    closest=computeClosest(coord)
    common=closest.intersection(data)
    print(common)
    c+=(6-len(common))
print(c)
