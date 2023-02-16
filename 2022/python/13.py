import ast
import numpy

def comparePackets(p1, p2):    
    if type(p1)==int and type(p2)==int:
        if p1<p2:
            return True
        elif p1>p2:
            return False
        return None
    elif type(p1)!=int and type(p2)==int:
        return comparePackets(p1, [p2])
    elif type(p1)==int and type(p2)!=int:
        return comparePackets([p1], p2)

    current=True
    c=0
    for i,j in zip(p1,p2):
        current=comparePackets(i,j)
        if current!=None:
            return current
        c+=1
    if c==len(p1) and c==len(p2):
        return None
    if c==len(p1):
        return True
    elif c==len(p2):
        return False    
        

def parse(lines):
    data=[]
    pair=[]
    for line in lines:
        if line=='\n':
            data.append(list(pair))
            pair.clear()
        else:
            pair.append(ast.literal_eval(line))
    return data

def starOne(pairs):
    c=1
    out=0
    for pair in pairs:
        if comparePackets(pair[0], pair[1]):
            out+=c
        c+=1
    return out

def starTwo(pairs):
    ordered=[]
    tmp=[]
    for pair in pairs:
        tmp.append(pair[0])
        tmp.append(pair[1])
    ordered.append(ast.literal_eval('[[2]]'))
    ordered.append(ast.literal_eval('[[6]]'))
    for i in range(len(tmp)):
        a=True
        for j in range(len(ordered)):
            if (not numpy.array_equal(tmp[i], ordered[j])) and comparePackets(tmp[i], ordered[j]):
                ordered.insert(j, tmp[i])
                a=False
                break
        if a:
            ordered.append(tmp[i])     
    ret=1
    for i in range(len(ordered)):
        tmp=ordered[i]
        
        if len(tmp)==1 and type(tmp[0])==list and len(tmp[0])==1 and tmp[0][0]==2:
            ret*=(i+1)
        if len(tmp)==1 and type(tmp[0])==list and len(tmp[0])==1 and tmp[0][0]==6:
            ret*=(i+1)
        
    return ret


file1=open('../inputs/input13')
lines=file1.readlines()

pairs=parse(lines)
print(starOne(pairs))
print(starTwo(pairs))