from collections import counter
def sh(s,y):
	return sum((Counter(s) & Counter(y)).values())

print(sh(s,y))

#to find common char in two strings 