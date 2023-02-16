smallest_j=100000
bigest_j=0
smallest_i=0
bigest_i=0



def parse(lines):
    
    global smallest_j
    global bigest_j
    global smallest_i
    global bigest_i
    #leer max i min 
    for line in lines:
        line=line.replace("\n", '')
        splited=line.split(' -> ')
        #print(splited)
        for s in splited:            
            splited2=s.split(',')
            if int(splited2[0])<smallest_j:
                smallest_j=int(splited2[0])
            if bigest_j<int(splited2[0]):
                bigest_j=int(splited2[0])
            #if int(splited2[1])<smallest_i:
            #    smallest_i=int(splited2[1])
            if bigest_i<int(splited2[1]):
                bigest_i=int(splited2[1])

    #expand map for abyss
    #smallest_j-=1
    #bigest_i+=1
    #bigest_j+=1

    #expand map for starTwo
    smallest_j-=300
    bigest_i+=2
    bigest_j+=300

    global factor_j
    factor_j=bigest_j-smallest_j
    global factor_i
    factor_i=bigest_i-smallest_i

    dataNormalized=[]
    lineCnt=0

    #crear mapa
    mapa=[]
    for i in range(factor_i+1):
        mapa.append([])
        for j in range(factor_j+1):
            if i==factor_i:
                mapa[i].append('#')
            else:
                mapa[i].append('.')
    
        
    #normalizar
    for line in lines:
        dataNormalized.append([])
        line=line.replace("\n",'')
        splited=line.split(' -> ')
        coord=0
        for s in splited:      
            splited2=s.split(',')
            dataNormalized[lineCnt].append([])
            splited2=s.split(',')
            dataNormalized[lineCnt][coord].append(int(splited2[1])) #1
            dataNormalized[lineCnt][coord].append(int(splited2[0])-(bigest_j-factor_j)) #0
            coord+=1
        lineCnt+=1

    #llenar mapa
    for rock in dataNormalized:
        for k in range(1,len(rock)):
            current=rock[k-1]
            mapa[current[0]][current[1]]='#'
            while rock[k]!=current:
                if current[0]<rock[k][0]:
                    current[0]+=1
                elif current[1]<rock[k][1]:
                    current[1]+=1
                elif current[0]>rock[k][0]:
                    current[0]-=1
                elif current[1]>rock[k][1]:
                    current[1]-=1
                mapa[current[0]][current[1]]='#'
    printMap(mapa)
    return mapa
    

def printMap(mapa):
    for l in mapa:
        for m in l:
            print(m, end='')
        print('')


def starOne(mapa):
    abyss=False
    c=0
    while not abyss:
        sand=[0,500-(bigest_j-factor_j)]
        #compute grain of sand until rest or abyss
        abyss=computeSand1(sand, mapa)
        #print map
        c+=1
    printMap(mapa)
    return c-1

def starTwo(mapa):
    blocked=False
    c=0
    while not blocked:
        sand=[0,500-(bigest_j-factor_j)]
        #compute grain of sand until rest or abyss
        blocked=computeSand2(sand, mapa)
        c+=1
        if c%10000==0:
            printMap(mapa)
    return c
            
def computeSand1(sand, mapa):
    #calculate next position, if None, abyss, else process
    if checkAbyss(sand):
        return True
    if sandResting(sand, mapa):
        return False
    next=nextPos(sand, mapa)
    return computeSand1(next, mapa)
    
def computeSand2(sand, mapa):
    #calculate next position, if None, abyss, else process
    if sandResting(sand, mapa) and checkBlocked(sand):
        return True
    if sandResting(sand, mapa):
        mapa[sand[0]][sand[1]]='o'
        return False
    next=nextPos(sand, mapa)
    return computeSand2(next, mapa)

def sandResting(sand, mapa):
    if ((mapa[sand[0]+1][sand[1]]=='#' or mapa[sand[0]+1][sand[1]]=='o') and
        (mapa[sand[0]+1][sand[1]-1]=='#' or mapa[sand[0]+1][sand[1]-1]=='o') and
        (mapa[sand[0]+1][sand[1]+1]=='#' or mapa[sand[0]+1][sand[1]+1]=='o')):
        return True
    return False
    
def checkAbyss(sand):
    if sand[0]==bigest_i or sand[1]==0 or sand[1]==bigest_j:
        return True
    return False

def checkBlocked(sand):
    if sand[0]==0 and sand[1]==500-(bigest_j-factor_j):
        return True
    return False

def nextPos(sand, mapa):
    if mapa[sand[0]+1][sand[1]]=='.':
        return [sand[0]+1,sand[1]]
    if mapa[sand[0]+1][sand[1]-1]=='.':
        return [sand[0]+1,sand[1]-1]
    return [sand[0]+1,sand[1]+1]

file1=open('../inputs/input14')
lines=file1.readlines()
mapa=parse(lines)
#print(starOne(mapa))
print(starTwo(mapa))