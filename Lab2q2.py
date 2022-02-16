#WAP to remove left recursion of the grammar.
grammar = {}

def add(str):                               
    x = str.split("->")
    y = x[1]
    x.pop()
    z = y.split("|")
    x.append(z)
    grammar[x[0]]=x[1]

def removeDirectLR(dict, A):        
	#dict is dictonary
	temp = dict[A]
	tempCr = []
	tempInCr = []
	for i in temp:
		if i[0] == A:
			tempInCr.append(i[1:]+[A+"'"])
		else:
			tempCr.append(i+[A+"'"])
	tempInCr.append(["e"])
	dict[A] = tempCr
	dict[A+"'"] = tempInCr
	return dict


def checkForIndirect(dict, a, ai):
	if ai not in dict:
		return False 
	if a == ai:
		return True
	for i in dict[ai]:
		if i[0] == ai:
			return False
		if i[0] in dict:
			return checkForIndirect(dict, a, i[0])
	return False

def rep(dict, A):
	temp = dict[A]
	newTemp = []
	for i in temp:
		if checkForIndirect(dict, A, i[0]):
			t = []
			for k in dict[i[0]]:
				t=[]
				t+=k
				t+=i[1:]
				newTemp.append(t)

		else:
			newTemp.append(i)
	dict[A] = newTemp
	return dict

def rem(grammar):
	c = 1
	conv = {}
	dict = {}
	revconv = {}
	for j in grammar:
		conv[j] = "A"+str(c)
		dict["A"+str(c)] = []
		c+=1

	for i in grammar:
		for j in grammar[i]:
			temp = []	
			for k in j:
				if k in conv:
					temp.append(conv[k])
				else:
					temp.append(k)
			dict[conv[i]].append(temp)

	for i in range(c-1,0,-1):
		ai = "A"+str(i)
		for j in range(0,i):
			aj = dict[ai][0][0]
			if ai!=aj :
				if aj in dict and checkForIndirect(dict,ai,aj):
					dict = rep(dict, ai)

	for i in range(1,c):
		ai = "A"+str(i)
		for j in dict[ai]:
			if ai==j[0]:
				dict = removeDirectLR(dict, ai)
				break

	op = {}
	for i in dict:
		a = str(i)
		for j in conv:
			a = a.replace(conv[j],j)
		revconv[i] = a

	for i in dict:
		l = []
		for j in dict[i]:
			k = []
			for m in j:
				if m in revconv:
					k.append(m.replace(m,revconv[m]))
				else:
					k.append(m)
			l.append(k)
		op[revconv[i]] = l

	return op

n = int(input("Enter No of Production: "))
for i in range(n):
    txt=input()
    add(txt)
   
result = rem(grammar)

for x,y in result.items():
    print(f'{x} -> {y}')

## To understand the output
##  'e' means ϵ (epsilon)
## A -> tA' | b is denoted as  A->[[‘t’,’A'’],[‘b’]]            
