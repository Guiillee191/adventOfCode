

def starOneNTwo(cards, numbers, mode):
	winnerCards=[]
	winnerNums=[]
	k=0
	for number in numbers:
		for c in range(len(cards)):
			for i in range(len(cards[c])):
				for j in range(len(cards[c][i])):
					if number==cards[c][i][j]:
						cards[c][i][j]='-1'
		
			if cardWon(cards[c]):
				
				if mode==0:
					return int(number)*unchecked(cards[c])
				else:
					if winnerCards.count(cards[c])==0:
						k+=1
						winnerCards.append(cards[c])
						winnerNums.append(number)
				if k==len(cards):
					
					return int(winnerNums[-1])*unchecked(winnerCards[-1])

def unchecked(card):
	c=0
	for i in range(len(card)):
		for j in range(len(card[i])):
			if card[i][j]!='-1':
				c+=int(card[i][j])
	return c

def cardWon(card):
	c=0
	d=0
	for i in range(len(card)):
		for j in range(len(card[i])):
			if card[i][j]=='-1':
				c+=1
			if card[j][i]=='-1':
				d+=1
		if c==(len(card[i])) or d==(len(card[j])):
			return True
		c=0
		d=0

#def starTwo():


cards=[]
card=[]
file1=open('../inputs/input4')
lines=file1.readlines()

numbers=lines[0].split(',')

j=0
for i in range(len(lines)-3):
	c=0
	if lines[i+2]=='\n':
		cards.append(card)
		card=[]
	else:
		card.append(lines[i+2].split())
	
print(starOneNTwo(cards, numbers, 1))
