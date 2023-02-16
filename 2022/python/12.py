file1=open('../inputs/test')
lines=file1.readlines()
data=[]
visited=[]
pathsToEnd=[]

for line in lines:
    tmp=[]
    for letter in line:
        tmp.append(letter)
    data.append(tmp)


for i in range(len(data)):
    visited.append([])
    for j in range(len(data[i])):
        visited[i].append(False)

print(visited)

for i in data:
    for j in i:
        print(j, end='')
    print('', end='')
print('')

def starOne(mapa):
    explore(mapa, [], [0,0],0)

def explore(mapa, directions, position, k):

    while successor(position):