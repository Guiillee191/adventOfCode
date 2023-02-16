from anytree import AnyNode, RenderTree, PreOrderIter

valid=[]

def parse(lines):
	ID=0
	current=AnyNode(id=ID,name='/', size=0)
	ID+=1
	for line in lines:
		split=line.split()
		if split[0]=='$':
			if split[1]=='cd':
				if split[2]=='..':
					current=current.parent
				else:
					newNode=AnyNode(id=ID, name=split[2], size=0)
					newNode.parent=current
					current=newNode
					ID+=1	
		else:
			if split[0]!='dir':
				newNode=AnyNode(id=ID, name=split[1], size=int(split[0]))
				newNode.parent=current
				ID+=1
	root=current.root
	#print(RenderTree(root))
	return root

def starOne(root):
	out=0
	for n in PreOrderIter(root):
		if not n.is_leaf and n.size<=100000:
			out+=n.size
	return out

def starTwo(root):
	freeSpace=70000000 - root.size
	neededSpace=30000000 - freeSpace
	best=root.size
	print('needed: ', neededSpace)
	for n in PreOrderIter(root):
		if (not n.is_leaf) and n.size<best and n.size>=neededSpace:
			best=n.size
	return best

	

def setSizes(root):
	totalSize=0
	if root.is_leaf:
		return root.size
	for n in root.children:
		totalSize+=setSizes(n)
	root.size=totalSize
	return totalSize

file1=open('../inputs/input7')
lines=file1.readlines()
structure=parse(lines)
#print(RenderTree(structure))
setSizes(structure)
print(RenderTree(structure))
print(starOne(structure))
print(starTwo(structure))
file1.close()




























