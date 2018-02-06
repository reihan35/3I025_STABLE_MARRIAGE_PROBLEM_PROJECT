import random

def generePrefEtu(n):
	pref=[]
	
	for i in range(0,n):
		tmp=[]
		for j in range(0,9): 
			r=random.randint(0,8)
			while(r in tmp):
				r=random.randint(0,8)
				
			tmp.append(r)
		print(tmp)
		pref.append(tmp)
		
	return pref


def generePrefParcours(n):
	pref = []
	cap = []
	
	sum_cap = 0
	
	for i in range(0, 9):
		cap.append(round(n/9))
		
	cap[random.randint(0, 8)] += n % 9
	print(cap)

	for i in range(0,9):
		tmp = []
		for j in range(0,n): 
			r=random.randint(0,n-1)
			while(r in tmp):
				r=random.randint(0,n-1)
				
			tmp.append(r)
		print(tmp)
		pref.append(tmp)
		
	return pref, cap
	
pref, cap = generePrefParcours(11)
