def starOne(data):
	#chunks={'(':0,'[':0,'{':0,'<':0,')':0,']':0,'}':0,'>':0}
	chunks={'(':')','[':']','{':'}','<':'>'}
	values={')':3,']':57,'}':1197,'>':25137}
	expected=[]
	score=0
	for line in data:
		for c in line:
			if c=='(' or c=='[' or c=='{' or c=='<':
				expected.append(chunks[c])
			else:
				if c!=expected[-1]:
					print('expected: ' + expected[-1] + ', seen: ' + c)
					score+=values[c]
					break
				else:
					expected.pop()
	return score

def starTwo(data):

	chunks={'(':')','[':']','{':'}','<':'>'}
	values={')':1,']':2,'}':3,'>':4}
	expected=[]
	scores=[]
	for line in data:
		for c in line:
			if c=='(' or c=='[' or c=='{' or c=='<':
				expected.append(chunks[c])
			else:
				if c!=expected[-1]:
					expected.clear()
					break
				else:
					expected.pop()
		if expected:
			score=0
			for c in reversed(expected):
				score=score*5+values[c]
			expected.clear()
			scores.append(score)
	scores.sort()
	return scores[int(len(scores)/2)]
					

file1=open('../inputs/input10')
lines=file1.readlines()
data=[]
for line in lines:
	data.append(line.replace('\n', ''))
print(starOne(data))
print(starTwo(data))
