from matrice import *
from gs import *

def calcule_util(etu,master,matrice):
	return 9-matrice[etu].index(master)
	
matriceEtu,nbEtu, matriceMaster,nbSpe = createMatrices("TestPrefEtu.txt","TestPrefSpe.txt")
print(calcule_util(0,5,matriceEtu))



def couples_util(matrice,k):
	E = []
	
	for j in range(0, len(matrice)):
		for i in range(1, len(matrice[j])):
			utilite = calcule_util(j, matrice[j][i], matrice)
			if utilite >= k:
				E.append([j, matrice[j][i], utilite])
				
	return E
	
def genere_lp(matriceEtu, matriceSpe, k):
	n = len(matriceEtu)
	E = couples_util(matriceEtu, k)
	filename = "plne" + str(k) + ".lp"
	f = open(filename, 'w')
	
	
	maximize = ""
	for c in E:
		maximize += " x" + str(c[0]) + "_" + str(c[1]) + " +"
	
	maximize = maximize[:-1]
	
	
	f.write("Maximize\n")
	f.write("obj:" + maximize + "\n")
	
	f.write("Subject To\n")
	
	for i in range(0, n): #pour chaque etudiant 
		couples_i = []
		for c in E:
			if i == c[0]:
				couples_i.append(c)
				
		sum_i = ""
		for c in couples_i:
			sum_i += " x" + str(c[0]) + "_" + str(c[1]) + " +"
		
		sum_i = sum_i[:-2]
		sum_i += " <= 1"
		f.write("c" + str(i+1) + ":" + sum_i + "\n")
		
	for j in range(0, 9): #pour chaque master
		i += 1
		couples_j = []
		for c in E:
			if j == c[1]:
				couples_j.append(c)

		sum_j = ""
		
		for c in couples_j:
			sum_j += " x" + str(c[0]) + "_" + str(c[1]) + " +"
		
		sum_j = sum_j[:-2]
		sum_j += " <= " + str(matriceSpe[len(matriceSpe)-1][j])
		f.write("c" + str(i+1) + ":" + sum_j + "\n")
	
	f.write("Bounds\n")
	for c in E:
		f.write("0 <= x" + str(c[0]) + "_" + str(c[1]) + " <= 1\n")
		
	
	f.write("Binary\n")
	x = ""
	for c in E:
		x += "x" + str(c[0]) + "_" + str(c[1]) + " "
	f.write(x + "\n")
	f.write("End\n")
	
	f.close()
	
E = couples_util(matriceEtu, 6)
print(E)

genere_lp(matriceEtu, matriceMaster, 5)
