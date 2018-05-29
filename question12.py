# a

def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True
		else:
			return False

def any_lowercase2(s):
	for c in s:
		if c.islower():
			return 'True'
		else:
			return 'False'

def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

def any_lowercase3(s):
	for c in s:
		flag = c.islower()
	return flag

s = ["Food"]


list1 = [-3,-2,-1,1,2,3,4,5,6,7,200,300,400]

def firstBad(aList):
	for i in range(0,len(aList)):
		if aList[i] < 0 or aList[i] > 100:
			return i
	return -1

print(firstBad(list1))